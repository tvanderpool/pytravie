from ._typing import _Instance, _Value
from typing import Generic, Callable, Optional, overload, Union, Type

class memoized_property(Generic[_Instance, _Value]):
    """A read-only @property that is only evaluated once."""
    __aname__: str = None    # type: ignore
    fget: Callable[[_Instance], _Value]

    def __init__(self, fget: Optional[Callable[[_Instance], _Value]] = None, doc=None, *, store_none=True):
        """ Called on initialisation of descriptor """
        if fget is not None:
            self.__set_fget(fget, doc)
        self.store_none = store_none

    def __set_fget(self, fget: Callable[[_Instance], _Value], doc=None):
        self.fget = fget
        self.__doc__ = doc or fget.__doc__
        if self.__aname__ is None:
            self.__aname__ = fget.__name__

    def __call__(self, fget: Callable[[_Instance], _Value]) -> "memoized_property":
        self.__set_fget(fget)
        return self

    @overload
    def __get__(self, instance: None, owner: Type[_Instance]) -> 'memoized_property':
        """ Called when an attribute is accessed via class not an instance """

    @overload
    def __get__(self, instance: _Instance, owner: Type[_Instance]) -> _Value:
        """ Called when an attribute is accessed on an instance variable """

    def __get__(self, instance: Union[_Instance, None], owner: Type[_Instance]) -> Union[_Value, 'memoized_property']:
        """ Full implementation is declared here """
        if instance is None: return self
        result = self.fget(instance)
        if self.store_none or result is not None:
            instance.__dict__[self.__aname__] = result
        return result

    def reset(self, instance: _Instance) -> None:
        instance.__dict__.pop(self.__aname__, None)    # type: ignore

    def __delete__(self, instance: _Instance) -> None:
        self.reset(instance)

    def HasValue(self, instance: _Instance):
        return self.__aname__ in instance.__dict__

    def __set_name__(self, owner: Type[_Instance], name: str):
        self.__aname__ = name
