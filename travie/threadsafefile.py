import threading

tls = threading.local()

class ThreadSafeFile(object):
    # __slots__ = ['f','lock']
    f = None
    lock = None
    def __init__(self, f):
        setattr( self, 'f', f )
        setattr( self, 'lock', threading.RLock() )
        # self.nesting = 0

    # def _getlock(self):
    #     self.lock.acquire()
    #     self.nesting += 1

    # def _droplock(self):
    #     nesting = self.nesting
    #     self.nesting = 0
    #     for i in range(nesting):
    #         self.lock.release()

    def __hasattr__(self, name):
        # print '__hasattr__', name
        return hasattr(self.f, name)

    def __getattr__(self, name):
        # print '__getattr__', name
        return getattr(self.f, name)

    def __setattr__(self, name, value):
        # print '__setattr__', name
        if name in ['f','lock']:
            object.__setattr__(self, name, value)
        else:
            setattr(self.f, name, value)

    def write(self, *args, **kwargs):
        with self.lock:
            self.f.write(*args, **kwargs)

    def flush(self, *args, **kwargs):
        with self.lock:
            self.f.flush(*args, **kwargs)


def make_stdout_threadsafe():
    from .threadsafefile import ThreadSafeFile
    import sys
    if type( sys.stdout ) is not ThreadSafeFile:
        sys.stdout = ThreadSafeFile( sys.stdout )


def make_stderr_threadsafe():
    from .threadsafefile import ThreadSafeFile
    import sys
    if type( sys.stderr ) is not ThreadSafeFile:
        sys.stderr = ThreadSafeFile( sys.stderr )
