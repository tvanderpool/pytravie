import atexit
import logging
import sys
import time
import weakref
import typing
if typing.TYPE_CHECKING:
    from .run_async_thread import RunAsyncThread

class WeakThreadSet(weakref.WeakSet["RunAsyncThread"]):
    def __iter__(self):
        threads_to_remove = weakref.WeakSet()
        for thread in super().__iter__():
            if thread.is_alive():
                yield thread
            else:
                threads_to_remove.add(thread)
        self.difference_update(threads_to_remove)

class __OnShutdown:
    _THREADS: WeakThreadSet
    _registered = False

    def __init__( self ):
        self._THREADS = WeakThreadSet()

    def register_thread(self, thread:"RunAsyncThread"):
        self._THREADS.add(thread)
        if not self._registered:
            atexit.register(_OnShutdown)
            self._registered = True

    @property
    def _ALIVE_THREADS(self):
        for t in self._THREADS:
            if not t.is_alive(): self._THREADS.remove(t)
        return self._THREADS

    def __call__( self, *args ):
        if not self._ALIVE_THREADS: return
        st = time.time()
        sys.stderr.write( 'Shutting Down Threads' )
        sys.stderr.flush()
        while len( self._ALIVE_THREADS ) and ( time.time() - st < 5 ):
            sys.stderr.write( '.' )
            sys.stderr.flush()
            logging.debug( 'run_async shutting down threads: %d', len( self._THREADS ) )
            for t in [*self._ALIVE_THREADS]:
                if t.is_alive: t.join( .5, stop=True)
                if not t.is_alive(): self._THREADS.remove(t)

        sys.stderr.write( '\n' )
        sys.stderr.flush()
        if self._THREADS:
            sys.exit(1)

_OnShutdown = __OnShutdown()
