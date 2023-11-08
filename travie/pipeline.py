import typing
if typing.TYPE_CHECKING:
    try:
        from typing import ParamSpec
    except ImportError:
        from typing_extensions import ParamSpec
    from typing import Callable, ParamSpec, TypeVar, List, Iterator, Generator
    _R_co = TypeVar('_R_co', covariant=True)
    _P = ParamSpec('_P')
from functools import partial, reduce, singledispatchmethod
import inspect
from ._pipeline_overloads import *

def __update_annotations(funcs):
    def update_annotations(func):
        sig0,sign = inspect.signature(funcs[0]), inspect.signature(funcs[-1])
        setattr(func,'__annotations__', {'input':next(iter(sig0.parameters.values())).annotation, 'return':sign.return_annotation})
        return func
    return update_annotations
def __reduce(arg,func): return func(arg)

def pipeline(func0, *funcs):
    __pipeline = partial(reduce, __reduce, (funcs:=(func0,)+funcs))
    @__update_annotations(funcs)
    def _pipeline(input: _TIn) -> _RLast:return __pipeline(input)
    return _pipeline

def pipe(input, func0, *funcs):
    return pipeline(func0, funcs)(input)

def _itGenChain(it, gen):return gen(it)

_BIND_FLAG = '__iter_pipeline_bind__'

class iter_pipeline(typing.Callable[_P, "Generator[_R_co, None, None]"]):
    _inner_gen:"Callable[_P, Generator[_R_co, None, None]]"
    _genwrappers:"List[Callable[[Iterator[_R_co]], Generator[_R_co, None, None]]]"

    def __init__(self, func0:"Callable[_P, Generator[_R_co, None, None]]", *funcs:"Callable[[Iterator[_R_co]], Generator[_R_co, None, None]]"):
        self._inner_gen, self._genwrappers = func0, list(funcs)

    def Pipe(self, wrapper:"Callable[[Iterator[_R_co]], Generator[_R_co, None, None]]", *additionalWrappers:"Callable[[Iterator[_R_co]], Generator[_R_co, None, None]]"):
        if wrapper is None: return partial(self._PipeWrapper, additionalWrappers)
        self._genwrappers += [ wrapper, *additionalWrappers]
        return self

    def _PipeWrapper(self, additionalWrappers:"Callable[[Iterator[_R_co]], Generator[_R_co, None, None]]", wrapper:"Callable[[Iterator[_R_co]], Generator[_R_co, None, None]]"):
        return self.Pipe(wrapper, *additionalWrappers)

    def InstancePipe(self, wrapper):
        setattr(wrapper, _BIND_FLAG, True)
        return self.Pipe(wrapper)

    def __call__(self, *args:"_P.args", **kwargs:"_P.kwargs"):
        return reduce( _itGenChain, self._genwrappers, self._inner_gen(*args, **kwargs) )

    def _BindGenWrappers(self, instance, owner):
        for F in self._genwrappers:
            match getattr(F, _BIND_FLAG, False):
                case True: yield F.__get__(instance, owner)
                case _: yield F

    def __get__(self, instance=None, owner=None):
        if instance is None: return self
        def boundcall(*args, **kwargs):
            return reduce(_itGenChain,
                          self._BindGenWrappers(instance, owner),
                          self._inner_gen.__get__(instance, owner)(*args, **kwargs))
        return boundcall

def iter_pipe(input, func0, *funcs):
    return iter_pipeline(func0, funcs)(input)

__all__ = 'pipe', 'pipeline', 'iter_pipe', 'iter_pipeline'
