import atexit
import logging
import sys
import threading
import time
import weakref

class _OnShutdown:
    _THREADS: weakref.WeakSet = []
    _registered = False

    def __init__( self ):
        self._THREADS = weakref.WeakSet()

    def register_thread(self, thread:threading.Thread):
        self._THREADS.add(thread)
        if not self._registered:
            atexit.register( _OnShutdown )
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
                if t.is_alive: t.join( .5, stop=True )
                if not t.is_alive(): self._THREADS.remove( t )

        sys.stderr.write( '\n' )
        sys.stderr.flush()
        if self._ALIVE_THREADS:
            sys.exit( 1 )

_OnShutdown = _OnShutdown()
