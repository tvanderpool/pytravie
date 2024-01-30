from .run_async import _run_async
import typing
import queue
if typing.TYPE_CHECKING:
    from typing import Callable, Generator, Iterator

_TQueueItem = typing.TypeVar("_TQueueItem")
__all__ = 'QueueThread', 'QueueThreadProcessor'

class QueueThread(_run_async.RunAsyncThread, typing.Generic[_TQueueItem]):
    def __init__(self, *args, **kwargs): # type: ignore
        super().__init__(*args, **kwargs)
        self.queue = queue.Queue()

    def _gen(self)->"Generator[_TQueueItem, None, None]":
        while not self.StopRequested:
            if (item:=self.queue.get()) is not None:
                yield item
            self.queue.task_done()
            if item is None:return

    def join(self, timeout=None):
        self.queue.join()
        return super().join( timeout, True )

    def Stop(self):
        if not self.StopRequested:
            self.queue.put(None)
        return super().Stop()

    def run(self):
        self._args = (self._gen(), *self._args)
        return super().run()

    def put(self, item:_TQueueItem, block=True, timeout=None):
        if self.StopRequested:
            raise Exception('Cannot add to stopped thread')
        return self.queue.put(item, block, timeout)
    def put_nowait(self, item:_TQueueItem):
        if self.StopRequested:
            raise Exception('Cannot add to stopped thread')
        return self.queue.put_nowait(item)
    def qsize(self)->int:
        return self.queue.qsize()

class QueueThreadProcessor( _run_async.RunAsyncBase[QueueThread[_TQueueItem]] ):
    def __init__( self, func:"Callable[[Iterator[_TQueueItem]], None]" ):
        super().__init__( func, True )
    # def __call__(self, *args, **kwargs)->Tuple[]:
    #     return super().__call__(*args, **kwargs)
    # @property
    # def StopRequested( self ):
    #     ct = threading.current_thread()
    #     if isinstance( ct, MyThread ) and ct._RunAsync == self:
    #         return ct.StopRequested

    # def __call__( self, *args, **kwargs ):
    #     thread = MyThread( target=self._func, args=args, kwargs=kwargs )
    #     thread.daemon = self._daemon
    #     thread._RunAsync = self
    #     self._threads.add( thread )
    #     thread.start()
    #     return thread

