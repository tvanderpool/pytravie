from builtins import aiter
import contextlib
from . import run_async
import typing
import asyncio
if typing.TYPE_CHECKING:
    from typing import Callable, AsyncGenerator, Coroutine, Any, AsyncIterator

_TQueueItem = typing.TypeVar("_TQueueItem")

class CloseableAsyncQueue(asyncio.Queue[_TQueueItem]):
    # _getters:typing.List[asyncio.Task[_TQueueItem]] = []
    _closed = False
    async def get(self):
        return await super().get()

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

    # def __anext__(self): return self.get()

class AQueueThread(run_async.RunAsyncThread, typing.Generic[_TQueueItem]):
    task:asyncio.Task = None
    tco:"Coroutine[Any,Any,None]"
    _loop:asyncio.AbstractEventLoop = None
    _stop_task:"asyncio.Future[None]"
    # _queue_get:asyncio.Task = None

    def __init__(self, **kwargs):
        super().__init__(daemon=kwargs.pop('daemon', True), **kwargs)
        self._queue = CloseableAsyncQueue()

    def join(self, timeout=None):
        super().join(timeout, True)

    def Stop(self):
        if not self.StopRequested:
            self._stop_task = asyncio.run_coroutine_threadsafe(self._queue.aclose(), self._loop)
        return super().Stop()

    async def _arun(self):
        self._loop = asyncio.get_running_loop()
        await self._target(aiter(self._queue), *self._args, **self._kwargs)

    def run(self):
        try:
            if self._target is not None:
                asyncio.run(self._arun())
        finally:
            del self._target, self._args, self._kwargs

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

del run_async, typing
