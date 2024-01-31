from typing import Callable, ParamSpec, TypeVar

_P = ParamSpec('_P')
_R = TypeVar('_R')
_F = Callable[_P, _R]

def Unwrap(func:Callable[[], _F])->_F:
    '''
    Unwrap a function that returns a function.
    '''
    return func()
