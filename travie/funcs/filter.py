import typing
if typing.TYPE_CHECKING:
    from ._typing import *

def Filter( items, op=None, key=None, val=None, Not=False, item=None, attr=None ):
    # print dict(op=op, key=key, val=val, Not=Not, item=item, attr=attr)
    if not callable( op ) and ( key is not None or item is not None or attr is not None ):
        from ._getop import _GetOp
        op = _GetOp( op, key, item, attr )
    # print dict(op=op, key=key, val=val, Not=Not, item=item, attr=attr)
    if op is not None and val is not None:
        from . import poperator
        op = poperator.chain( op, poperator.eq( val ) )
    if op is not None and Not: op = poperator.not_( op )
    # print dict(op=op, key=key, val=val, Not=Not, item=item, attr=attr)
    return list( filter( op, list( items ) ) )


def FilterNone( items ):
    from . import poperator
    return list( filter( poperator.isNone( False ), list( items ) ) )
