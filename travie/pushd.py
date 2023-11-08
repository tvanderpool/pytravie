import contextlib
import os
__all__ = ['pushd', 'pushdctx', 'popd']
dirs=[]
@contextlib.contextmanager
def pushdctx(new_dir):
    old_dir = os.getcwd()
    if os.path.isfile(new_dir):
        new_dir = os.path.dirname(new_dir)
    os.chdir(new_dir)
    try:
        yield
    finally:
	    os.chdir(old_dir)

def pushd(new_dir):
    dirs.append(os.getcwd())
    if os.path.isfile(new_dir):
        new_dir = os.path.dirname(new_dir)
    os.chdir(new_dir)
    
def popd():
    if dirs: os.chdir(dirs.pop())