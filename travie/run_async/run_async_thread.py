from typing import Optional, TypeVar, TYPE_CHECKING
from functools import wraps
import threading
from ._OnShutdown import _OnShutdown
if TYPE_CHECKING:
    from ._run_async import RunAsyncBase


class RunAsyncThread( threading.Thread ):
    _RunAsync:Optional["RunAsyncBase"] = None

    @wraps( threading.Thread.__init__ )
    def __init__( self, *args, **kwargs ):
        """ constructor, setting initial variables """
        # print args,kwargs
        # traceback.print_stack()
        self._stopevent = threading.Event()
        # self._sleepperiod = 1.0
        threading.Thread.__init__( self, *args, **kwargs )
        _OnShutdown.register_thread( self )

    @property
    def StopRequested( self ):
        return self._stopevent.isSet()

    def Stop( self ):
        return self._stopevent.set()

    def join( self, timeout=None, stop=False ):
        """ Stop the thread. """
        if stop: self.Stop()
        return super().join( timeout )

TThread = TypeVar( "TThread", bound=RunAsyncThread )
