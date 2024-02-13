from ._typing import _Instance, _Value
from typing import Generic, Callable, Optional, Union, Type

class memoized_classproperty(Generic[_Instance, _Value]):
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

    def __call__(self, fget: Callable[[_Instance], _Value]) -> "memoized_classproperty":
        self.__set_fget(fget)
        return self

    def __get__(self, instance: Union[_Instance, None], owner: Type[_Instance]) -> _Value:
        """ Full implementation is declared here """
        result = self.fget(instance)
        if self.store_none or result is not None:
            instance.__dict__[self.__aname__] = result
            cls = instance.__class__ if instance is not None else owner
            setattr(cls, self.__name__, result := self.fget(owner))
        return result

    def __set_name__(self, owner: Type[_Instance], name: str):
        self.__aname__ = name
