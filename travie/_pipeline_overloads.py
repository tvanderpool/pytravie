from functools import partial, reduce, singledispatchmethod
import inspect
from typing import Any, Callable, Generator, Iterator, List, Literal, ParamSpec, Tuple, TypeVar, overload
_TIn = TypeVar('_TIn')
_RLast = TypeVar('_RLast')
_R0 = TypeVar('_R0')
_R1 = TypeVar('_R1')
_R2 = TypeVar('_R2')
_R3 = TypeVar('_R3')
_R4 = TypeVar('_R4')
_R5 = TypeVar('_R5')
_R6 = TypeVar('_R6')
_R7 = TypeVar('_R7')
_R8 = TypeVar('_R8')
_R9 = TypeVar('_R9')
_R10 = TypeVar('_R10')
_R11 = TypeVar('_R11')
_R12 = TypeVar('_R12')
_R13 = TypeVar('_R13')
_R14 = TypeVar('_R14')
_R15 = TypeVar('_R15')
_R16 = TypeVar('_R16')
_R17 = TypeVar('_R17')
_R18 = TypeVar('_R18')
_R19 = TypeVar('_R19')
_R20 = TypeVar('_R20')
@overload
def pipeline(func0:Callable[[_TIn], _RLast])->Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12],_R13], func14:Callable[[_R13],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12],_R13], func14:Callable[[_R13],_R14], func15:Callable[[_R14],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12],_R13], func14:Callable[[_R13],_R14], func15:Callable[[_R14],_R15], func16:Callable[[_R15],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12],_R13], func14:Callable[[_R13],_R14], func15:Callable[[_R14],_R15], func16:Callable[[_R15],_R16], func17:Callable[[_R16],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12],_R13], func14:Callable[[_R13],_R14], func15:Callable[[_R14],_R15], func16:Callable[[_R15],_R16], func17:Callable[[_R16],_R17], func18:Callable[[_R17],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12],_R13], func14:Callable[[_R13],_R14], func15:Callable[[_R14],_R15], func16:Callable[[_R15],_R16], func17:Callable[[_R16],_R17], func18:Callable[[_R17],_R18], func19:Callable[[_R18],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipeline(func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12],_R13], func14:Callable[[_R13],_R14], func15:Callable[[_R14],_R15], func16:Callable[[_R15],_R16], func17:Callable[[_R16],_R17], func18:Callable[[_R17],_R18], func19:Callable[[_R18],_R19], func20:Callable[[_R19],_RLast]) -> Callable[[_TIn], _RLast]: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12],_R13], func14:Callable[[_R13], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12],_R13], func14:Callable[[_R13],_R14], func15:Callable[[_R14], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12],_R13], func14:Callable[[_R13],_R14], func15:Callable[[_R14],_R15], func16:Callable[[_R15], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12],_R13], func14:Callable[[_R13],_R14], func15:Callable[[_R14],_R15], func16:Callable[[_R15],_R16], func17:Callable[[_R16], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12],_R13], func14:Callable[[_R13],_R14], func15:Callable[[_R14],_R15], func16:Callable[[_R15],_R16], func17:Callable[[_R16],_R17], func18:Callable[[_R17], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12],_R13], func14:Callable[[_R13],_R14], func15:Callable[[_R14],_R15], func16:Callable[[_R15],_R16], func17:Callable[[_R16],_R17], func18:Callable[[_R17],_R18], func19:Callable[[_R18], _RLast]) -> _RLast: ...
@overload
def pipe(input: _TIn, func0:Callable[[_TIn], _R0], func1:Callable[[_R0],_R1], func2:Callable[[_R1],_R2], func3:Callable[[_R2],_R3], func4:Callable[[_R3],_R4], func5:Callable[[_R4],_R5], func6:Callable[[_R5],_R6], func7:Callable[[_R6],_R7], func8:Callable[[_R7],_R8], func9:Callable[[_R8],_R9], func10:Callable[[_R9],_R10], func11:Callable[[_R10],_R11], func12:Callable[[_R11],_R12], func13:Callable[[_R12],_R13], func14:Callable[[_R13],_R14], func15:Callable[[_R14],_R15], func16:Callable[[_R15],_R16], func17:Callable[[_R16],_R17], func18:Callable[[_R17],_R18], func19:Callable[[_R18],_R19], func20:Callable[[_R19], _RLast]) -> _RLast: ...

__all__ = '_TIn','_RLast','_R0','_R1','_R2','_R3','_R4','_R5','_R6','_R7','_R8','_R9','_R10','_R11','_R12','_R13','_R14','_R15','_R16','_R17','_R18','_R19','_R20',
