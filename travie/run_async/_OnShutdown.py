import atexit
import logging
import sys
import threading
import time
import weakref

THREADS: weakref.WeakSet[threading.Thread] = weakref.WeakSet()

def _OnShutdown(*args):
    global THREADS
    THREADS = [t for t in THREADS if t.is_alive()]
    if THREADS: return
    st = time.time()
    sys.stderr.write( 'Shutting Down Threads' )
    sys.stderr.flush()
    while len( THREADS ) and ( time.time() - st < 5 ):
        sys.stderr.write( '.' )
        sys.stderr.flush()
        logging.debug( 'run_async shutting down threads: %d', len( THREADS ) )
        for t in list( THREADS ):
            if t.is_alive: t.join( .5, stop=True )
            if not t.is_alive(): THREADS.remove( t )

    sys.stderr.write( '\n' )
    sys.stderr.flush()
    if [t for t in THREADS if t.is_alive()]:
        sys.exit( 1 )
atexit.register( _OnShutdown )
