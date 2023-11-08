import typing
if typing.TYPE_CHECKING:
    from ._typing import *
from ._group_by_easy_overloads import *
from ._getop import _GetOp
from .sorted import Sorted

def GroupByEasy( iterable:"Iterable[IterItemT]", *,
                sort:"bool"=False,
key:"Optional[Callable[[IterItemT],KT]]"=None,
op:"Optional[Union[str,Any]]"=None,
item:"Optional[Any]"=None,
attr:"Optional[str]"=None,
vkey:"Optional[Callable[[IterItemT],VT]]"=None,
vop:"Optional[Union[str,Any]]"=None,
vitem:"Optional[Any]"=None,
vattr:"Optional[str]"=None
                )->"Generator[Tuple[KT,Union[IterItemT,VT]],None,None]":
    import itertools
    KeyF:"Callable[[IterItemT],KT]" = _GetOp( op, key, item, attr )
    VKeyF:"Union[Callable[[IterItemT],VT],None]" = _GetOp( vop, vkey, vitem, vattr )
    g2list:"Callable[[Iterable[IterItemT]],VT]" = (lambda G:[VKeyF(r) for r in G ]) if VKeyF else list
    yield from ( ( k, g2list( g ) ) for k, g in itertools.groupby( ( Sorted( iterable, key=KeyF, op=op ) if sort else iterable ), KeyF ) )



