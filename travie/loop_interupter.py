import signal

LOOP_EXIT_REQUESTED=False

def handler(signum, frame):
    global LOOP_EXIT_REQUESTED
    LOOP_EXIT_REQUESTED=True
    print( 'LOOP_EXIT_REQUESTED' )
signal.signal(signal.SIGQUIT, handler)
