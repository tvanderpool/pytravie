import threading
from typing import Generic, Type
import typing
import weakref
from .run_async_thread import TThread, RunAsyncThread
# def _run_async(func, daemon):
#     @wraps(func)
#     def async_func( *args, **kwargs ):
#         func_hl = MyThread( target=func, args=args, kwargs=kwargs )
#         func_hl.daemon = daemon
#         func_hl.start()
#         return func_hl
#     return async_func

class _RunAsync( Generic[TThread] ):
    _threads = []

    def __init__( self, func, daemon=False ):
        self._func = func
        self._daemon = daemon
        self._threads = weakref.WeakSet()

    def StopAll( self ):
        for t in self._threads:
            if t.is_alive():
                t._stopevent.set()

    @property
    def StopRequested( self ):
        if isinstance( ct:=threading.current_thread(), RunAsyncThread ) and ct._RunAsync == self:
            return ct.StopRequested

    @classmethod
    @property
    def _ThreadCls(cls)->Type[TThread]:
        if ob:=getattr(cls,'__orig_bases__',None):
            if obargs:=typing.get_args(ob[0]):
                return obargs[0]
        return RunAsyncThread
        # return obargs[0] if (ob:=getattr(cls,'__orig_bases__',None)) and (obargs:=typing.get_args(ob[0])) else MyThread

    def __call__( self, *args, **kwargs )->TThread:
        thread = self._ThreadCls( target=self._func, args=args, kwargs=kwargs )
        thread.daemon = self._daemon
        thread._RunAsync = self
        self._threads.add( thread )
        thread.start()
        return thread


class run_async( _RunAsync[RunAsyncThread] ):

    def __init__( self, func ):
        super().__init__( func, False )


class run_async_daemon( _RunAsync[RunAsyncThread] ):

    def __init__( self, func ):
        super().__init__( func, True )


RunAsync, RunAsyncDaemon = run_async, run_async_daemon
