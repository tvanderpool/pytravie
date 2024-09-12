import typing
if typing.TYPE_CHECKING:
    from ._typing import *
from .filter import FilterNone

def _GetOp( op, key:"Optional[Callable[[IterItemT],VT]]", item:"Optional[KT]", attr:"Optional[str]" )->"Callable[[IterItemT],VT]":
    argc = len( FilterNone( [ op, item, attr ] ) )
    if argc == 0: return key
    assert argc == 1, 'op, item, attr are exclusive arguments'
    import operator
    from .. import poperator
    if item is not None:
        op = 'item'
        key = item
    elif attr is not None:
        op = 'attr'
        key = attr
    if op in ( 'attr', 'item' ): op += 'getter'
    return getattr( ( poperator if hasattr( poperator, op ) else operator ), op )( key )
