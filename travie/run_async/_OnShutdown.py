import atexit
import logging
import sys
import threading
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

class _OnShutdown:
    _THREADS: WeakThreadSet
    _registered = False

    def __init__( self ):
        self._THREADS = WeakThreadSet()

    def register_thread(self, thread:"RunAsyncThread"):
        self._THREADS.add(thread)
        if not self._registered:
            atexit.register( _OnShutdown ) # this isn't adding the class, because this is a singleton
            self._registered = True

    def __call__( self, *args ):
        if not any(self._THREADS): return
        st = time.time()
        sys.stderr.write( 'Shutting Down Threads' )
        sys.stderr.flush()
        while any( self._THREADS ) and ( time.time() - st < 5 ):
            sys.stderr.write( '.' )
            sys.stderr.flush()
            logging.debug( 'run_async shutting down threads: %d', len( self._THREADS ) )
            for t in self._THREADS:
                t.join( .5, stop=True )

        sys.stderr.write( '\n' )
        sys.stderr.flush()
        if any(self._THREADS):
            sys.stderr.write( 'threads still running\n' )
            sys.stderr.flush()
            # exit( 0 )

_OnShutdown = _OnShutdown()
