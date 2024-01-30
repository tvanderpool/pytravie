from builtins import aiter
import contextlib
from . import run_async
import typing
import asyncio
from threading import Event
if typing.TYPE_CHECKING:
    from typing import Callable, Coroutine, Any, AsyncIterator
    import concurrent.futures

_TQueueItem = typing.TypeVar("_TQueueItem")

class CloseableAsyncQueue(asyncio.Queue[_TQueueItem]):
    _closed = False
    # _getters:typing.List[asyncio.Task[_TQueueItem]] = []
    # def get(self) -> typing.Awaitable[_TQueueItem]:
    #     self._getters.append(gett := asyncio.create_task(super().get()))
    #     gett.add_done_callback(self._getters.remove)
    #     return gett

    async def aclose(self):
        self._closed = True
        await self.join()
        gett:asyncio.Future
        for gett in self._getters: gett.cancel()

    async def put(self, item: _TQueueItem) -> None:
        if self._closed: raise Exception("Cannot add item to closed queue")
        return await super().put(item)

    def put_nowait(self, item: _TQueueItem) -> None:
        if self._closed: raise Exception("Cannot add item to closed queue")
        return super().put_nowait(item)

    async def __aiter__(self):
        with contextlib.suppress(asyncio.CancelledError):
            while True:
                yield await self.get()
                self.task_done()

class AQueueThread(run_async.RunAsyncThread, typing.Generic[_TQueueItem]):
    task:asyncio.Task|None = None
    tco:"Coroutine[Any,Any,None]"
    _loop:asyncio.AbstractEventLoop = None # type: ignore
    _stop_task:"concurrent.futures._base.Future[None]"
    _astarted:Event

    def __init__(self, queue:CloseableAsyncQueue|None=None, **kwargs):
        super().__init__(daemon=kwargs.pop('daemon', True), **kwargs)
        self._queue = queue or CloseableAsyncQueue()
        self._astarted = Event()

    def join(self, timeout=None, stop=True):
        super().join(timeout, stop)

    def Stop(self):
        if not self.StopRequested:
            if self._loop is not None and self._loop.is_running():
                self._stop_task = self._loop.call_soon_threadsafe(self._queue.aclose)
            else:
                self._queue.close()
        return super().Stop()
    
    async def _arun(self):
        self._loop = asyncio.get_running_loop()
        self._astarted.set()
        await self._target(aiter(self._queue), *self._args, **self._kwargs) # type: ignore

    def run(self):
        try:
            if self._target is not None: # type: ignore
                asyncio.run(self._arun())
        finally:
            del self._target, self._args, self._kwargs # type: ignore

    def put(self, item:_TQueueItem, block=True, timeout=None):
        if self.StopRequested:
            raise Exception('Cannot add to stopped thread')
        return asyncio.run_coroutine_threadsafe(self._queue.put(item), self._loop).result()
    
    def put_nowait(self, item:_TQueueItem):
        if self.StopRequested:
            raise Exception('Cannot add to stopped thread')
        return self._loop.call_soon_threadsafe(self._queue.put_nowait, item)
    
    def qsize(self)->int:
        return self._queue.qsize()

class AQueueThreadProcessor( run_async.RunAsyncBase[AQueueThread[_TQueueItem]] ):
    def __init__( self, func:"Callable[[AsyncIterator[_TQueueItem]], Coroutine[Any,Any,None]]" ):
        super().__init__( func, True )

    def __call__(self, *args, **kwargs) -> AQueueThread[_TQueueItem]:
        thread = super().__call__(*args, **kwargs)
        thread._astarted.wait()
        return thread

del run_async, typing
