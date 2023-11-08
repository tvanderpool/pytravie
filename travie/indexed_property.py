from functools import partial, wraps
import io
from typing import Callable
from memoized import memoized_property
import hashlib
import pickle
import inspect
import copyreg, copy, pickle

# hash(obj.__class__)
# 2967063
# hash(obj)
# 8764332649882

# class MyPickler( pickle.Pickler ):

#     def reducer_override( self, obj ):
#         try:
#             result = object.__reduce__( obj )
#             return result
#         except TypeError:
#             return NotImplemented
#         except AttributeError:
#             return NotImplemented

#     @classmethod
#     def dumps( cls, obj, protocol=None, *, fix_imports=True, buffer_callback=None ):
#         with io.BytesIO() as bio:
#             cls( bio, protocol, fix_imports=fix_imports, buffer_callback=buffer_callback ).dump( obj )
#             return bio.getvalue()


def ArgHash( func, *args, **kwargs ):
    callargs = inspect.getcallargs( func, *args, **kwargs )
    # callargs.pop( 'self', None )
    return hashlib.md5( pickle.dumps( callargs ) ).hexdigest()


# def memoized_instancemethod(func=None, *, cfunc=None):
#     def outer_wrapper(func):
#         def cache_wrapper(self, *args, **kwargs )
#     if func is None:
#         return outer_wrapper
#     return outer_wrapper(func)
#                 if cacheresults and (argKey := ArgHash( fgetitem, *args, **kwargs ) ) in self.cache:
#                     return self.cache[key]
#                 result = fgetitem( self.instance, key )
#                 if cacheresults:
#                     self.cache[key] = result


class memoized_instancemethod:
    _func: Callable = None
    cache: dict

    def __init__( self, func=None ):
        self.wrappedFunc = func
        self.cache = {}

    @property
    def wrappedFunc( self ) -> Callable:
        return self._func

    @wrappedFunc.setter
    def wrappedFunc( self, value: Callable ):
        if value is not None:
            wraps( value )( self )
        self._func = value

    def __call__( self, *args, **kwargs ):
        if self.wrappedFunc is None:
            self.wrappedFunc = args[0]
            return self
        if ( key := ArgHash( self.wrappedFunc, *args, **kwargs ) ) in self.cache:
            return self.cache[key]
        self.cache[key] = result = self.wrappedFunc( *args, **kwargs )
        return result

    def __reduce__( self ):
        result = super().__reduce__()
        return result


@partial( copyreg.pickle, memoized_instancemethod )
def __pickle_memoized_instancemethod( obj ):
    return memoized_instancemethod, ( obj.wrappedFunc, )


class IndexedProperty:
    name: str
    _fgetitem: Callable
    _cacheresults: bool
    _retType: type
    _indexers: dict

    @staticmethod
    def _MakeDescriptorIndexer( fgetitem: Callable, cacheresults: bool, retType: type ):

        class DescriptorIndexer( retType ):
            value: None

            def __new__( cls, *args, **kwargs ):
                kwargs.pop( 'instance' )
                return super().__new__( cls, *args, **kwargs )

            def __init__( self, value, *, instance ):
                if '__init__' in self.__class__.__base__.__dict__:
                    super().__init__( value )
                self.instance = instance
                self.value = value

            def __getitem__( self, key ):
                if type( key ) is tuple and len( key ) > 1:
                    return self( *key )
                if type( key ) is dict:
                    return self( **key )
                return self( key )

            def reset( self ):
                fgetitem.cache.clear()

            @wraps( fgetitem )
            def __call__( self, *args, **kwargs ):
                return fgetitem( self.instance, *args, **kwargs )

        if cacheresults:
            fgetitem = memoized_instancemethod( fgetitem )

        return DescriptorIndexer

    @property
    def DescriptorIndexer( self ):
        if self._retType is None or self._fgetitem is None:
            return None
        cls = IndexedProperty._MakeDescriptorIndexer( self._fgetitem, self._cacheresults, self._retType )
        self.__dict__['DescriptorIndexer'] = cls
        return cls

    @memoized_property
    def aname( self ):
        return f'_{self.name}'

    def __init__( self, fgetitem=None, *, cache=False, retType: type = None ):
        self._fgetitem = fgetitem
        self._cacheresults = cache
        self._retType = retType
        self._indexers = {}

    def __set_name__( self, owner, name ):
        self.name = name

    def __get__( self, instance, owner=None, *args, **kwargs ):
        if instance is None: return self
        # if not hasattr( instance, self.aname ):
        if instance not in self._indexers:
            value = self._fgetitem( instance )
            if value is None: return None
            if self.DescriptorIndexer is None:
                self._retType = type( value )
            # setattr( instance, self.aname, self.DescriptorIndexer( value, instance=instance ) )
            self._indexers[instance] = self.DescriptorIndexer( value, instance=instance )
        return self._indexers[instance]
        # return getattr( instance, self.aname )

    def __call__( self, fgetitem ):
        self._fgetitem = fgetitem
        return self

    def __getstate__( self ):
        return { k: v for k, v in self.__dict__ if k not in ( 'DescriptorIndexer', '_indexers' ) }


# @partial( copyreg.pickle, memoized_instancemethod )
# def __pickle_memoized_instancemethod( obj ):
#     return memoized_instancemethod, ( obj.wrappedFunc, )
