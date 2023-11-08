import typing
if typing.TYPE_CHECKING:
    from ._typing import *

# yapf:disable
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, key:"Callable[[IterItemT],KT]", sort:"bool"=False )->"Generator[Tuple[KT,IterItemT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, key:"Callable[[IterItemT],KT]", vkey:"Callable[[IterItemT],VT]", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, key:"Callable[[IterItemT],KT]", vop:"Union[str,Any]", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, key:"Callable[[IterItemT],KT]", vitem:"Any", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, key:"Callable[[IterItemT],KT]", vattr:"str", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, op:"Union[str,Any]", sort:"bool"=False )->"Generator[Tuple[KT,IterItemT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, op:"Union[str,Any]", vkey:"Callable[[IterItemT],VT]", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, op:"Union[str,Any]", vop:"Union[str,Any]", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, op:"Union[str,Any]", vitem:"Any", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, op:"Union[str,Any]", vattr:"str", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, item:"Any", sort:"bool"=False )->"Generator[Tuple[KT,IterItemT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, item:"Any", vkey:"Callable[[IterItemT],VT]", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, item:"Any", vop:"Union[str,Any]", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, item:"Any", vitem:"Any", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, item:"Any", vattr:"str", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, attr:"str", sort:"bool"=False )->"Generator[Tuple[KT,IterItemT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, attr:"str", vkey:"Callable[[IterItemT],VT]", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, attr:"str", vop:"Union[str,Any]", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, attr:"str", vitem:"Any", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
@typing.overload
def GroupByEasy( iterable:"Iterable[IterItemT]", *, attr:"str", vattr:"str", sort:"bool"=False )->"Generator[Tuple[KT,VT], None, None]":pass
# yapf:enable
