import typing
if typing.TYPE_CHECKING:
    from typing import List
from contextlib import contextmanager
from .group_by_easy import GroupByEasy
from .filter import FilterNone, Filter
from .sorted import Sorted, topological_sort

def readlines()->"List[str]":
    lines = []
    while tuple( lines[ -2: ] ) != ( '', '' ):
        lines.append( input() )
    return lines[ :-2 ]

class ValueHolder( object ):
    _value = None

    @property
    def value( self ):
        return self._value

    @value.setter
    def value( self, value ):
        self._value = value

    get = value.fget
    set = value.fset

@contextmanager
def time_it( label='', after=None ):
    import time
    from datetime import timedelta
    t = time.time()
    result = ValueHolder()
    yield result
    elapsed = time.time() - t
    if after:
        after( elapsed )
    else:
        print( label, timedelta( seconds=elapsed ), result.value )


def while_timeout( test, timeout=3, pause=.1, exitvalue=True ):
    import time

    def reset():
        reset.start_time = time.time()

    setattr( reset, 'start_time', time.time() )
    setattr( reset, 'value', None )

    def testerw():
        reset.value = test()
        if exitvalue == False:
            return not reset.value
        elif exitvalue != True:
            return reset.value == exitvalue
        else:
            return reset.value

    while not testerw() and ( time.time() - reset.start_time ) < timeout:
        with time_it( after=lambda e: time.sleep( max( pause - e, 0 ) ) ):
            yield reset


def do_until( target, condition, timeout=3, pause=1, exitvalue=True, _print=False ):
    for reset in while_timeout( condition, timeout, pause, exitvalue ):
        if _print:
            print( target() )
        else:
            target()

@contextmanager
def sameline( s=None ):
    if s: echo( s )
    yield None
    echo( '\n' )


def echo( s ):
    import sys
    sys.stdout.write( s )
    sys.stdout.flush()


def echoerr( s ):
    import sys
    sys.stderr.write( s )
    sys.stderr.flush()


def LoopPrinter( it ):
    for i in it:
        echo( '.' )
        yield i

def wrapif( v, prefix=' ', suffix=' ', not_='' ):
    if v: return '{}{}{}'.format( prefix, v, suffix )
    return not_

def filter_nones_from_dict( DICT={}, **kwargs ):
    return { k: v for k, v in list( DICT.items() ) + list( kwargs.items() ) if v is not None }

# class classproperty:
#     def __init__( self, getter ):
#         self.getter = getter

#     def __get__( self, instance, owner ):
#         return self.getter( owner )
def classproperty(func):
    return classmethod(property(func))
