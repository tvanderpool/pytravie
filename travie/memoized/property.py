from ._typing import *
from typing import Generic, Callable, Optional, overload, Union, Type

class memoized_property( Generic[ Instance, Value ] ):
    """A read-only @property that is only evaluated once."""
    __aname__: str = None    # type: ignore
    fget: Callable[ [ Instance ], Value ]

    def __init__( self, fget: Optional[ Callable[ [ Instance ], Value ] ] = None, doc=None, *, store_none=True ):
        """ Called on initialisation of descriptor """
        if fget is not None:
            self.__set_fget( fget, doc )
        self.store_none = store_none

    def __set_fget( self, fget: Callable[ [ Instance ], Value ], doc=None ):
        self.fget = fget
        self.__doc__ = doc or fget.__doc__
        if self.__aname__ is None:
            self.__aname__ = fget.__name__

    def __call__( self, fget: Callable[ [ Instance ], Value ] ) -> "memoized_property":
        self.__set_fget( fget )
        return self

    @overload
    def __get__( self, instance: None, owner: Type[ Instance ] ) -> 'memoized_property':
        """ Called when an attribute is accessed via class not an instance """

    @overload
    def __get__( self, instance: Instance, owner: Type[ Instance ] ) -> Value:
        """ Called when an attribute is accessed on an instance variable """

    def __get__( self, instance: Union[ Instance, None ], owner: Type[ Instance ] ) -> Union[ Value, 'memoized_property' ]:
        """ Full implementation is declared here """
        if instance is None: return self
        result = self.fget( instance )
        if self.store_none or result is not None:
            instance.__dict__[ self.__aname__ ] = result
        return result

    # def __set__(self, instance: Instance, value: Value):
    #     """ Called when setting a value."""

    # @singledispatchmethod
    def reset( self, instance: Instance ) -> None:
        instance.__dict__.pop( self.__aname__, None )    # type: ignore

    def __delete__( self, instance: Instance ) -> None:
        self.reset( instance )

    def HasValue( self, instance: Instance ):
        return self.__aname__ in instance.__dict__

    # @classmethod
    # def reset( cls, owner: Type[ Instance ], name: str ):
    #     owner.__dict__.pop( name, None )    # type: ignore

    def __set_name__( self, owner: Type[ Instance ], name: str ):
        self.__aname__ = name

# class memoized_property( object ):
#     """A read-only @property that is only evaluated once."""

#     def __init__( self, fget, doc=None ):
#         self.fget = fget
#         self.__doc__ = doc or fget.__doc__
#         self.__name__ = fget.__name__

#     def __get__( self, obj, cls ):
#         if obj is None:
#             return self
#         obj.__dict__[ self.__name__ ] = result = self.fget( obj )
#         return result

#     def _reset( self, obj ):
#         memoized_property.reset( obj, self.__name__ )

#     @classmethod
#     def reset( cls, obj, name ):
#         obj.__dict__.pop( name, None )
