from typing import TypeVar
from functools import wraps
import threading
from . import _OnShutdown

class RunAsyncThread( threading.Thread ):
    _RunAsync = None

    @wraps( threading.Thread.__init__ )
    def __init__( self, *args, **kwargs ):
        """ constructor, setting initial variables """
        # print args,kwargs
        # traceback.print_stack()
        self._stopevent = threading.Event()
        # self._sleepperiod = 1.0
        threading.Thread.__init__( self, *args, **kwargs )
        _OnShutdown.THREADS( self )

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
