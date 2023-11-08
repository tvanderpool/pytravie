from .funcs import filter_nones_from_dict
import typing
if typing.TYPE_CHECKING:
    from typing import Type, Callable


def add_class_method( cls, method, name=None ):
    setattr( cls, name or method.__name__, classmethod( method ) )


def add_method( cls, method, name=None ):
    import six
    if six.PY3:
        setattr( cls, name or method.__name__, method )
    else:
        from types import MethodType
        setattr( cls, name or method.__name__, MethodType( method, None, cls ) )


def add_property( cls, name=None, fget=None, fset=None, fdel=None, doc=None ):
    if callable( name ):
        name, fget, fset, fdel, doc = None, name, fget, fset, fdel
    setattr( cls, name or fget.__name__, property( **filter_nones_from_dict( dict( fget=fget, fset=fset, fdel=fdel, doc=doc ) ) ) )

def ExtendCls( cls:"Type", name=None ):
    def ExtendCls( func:"Type"|"Callable" ):
        match func:
            case type() as klass:
                for fname, func in klass.__dict__.items():
                    if not(fname.startswith('__') or fname.endswith('__')):
                        ExtendCls( func )
                return
            case _ if name: fname = name
            case staticmethod(): fname = func.__func__.__name__
            case property() if hasattr(func, '__name__'): fname = func.__name__
            case property(): fname = func.fget.__name__
            case _:
                fname = func.__name__
        setattr( cls, fname, func )
        # return func
    return ExtendCls
