from travie.aqueue_thread import AQueueThreadProcessor
import time

@AQueueThreadProcessor
async def Processor(aiter):
    i = 0
    async for item in aiter:
        if (i:=i+1) >= 3:
            raise Exception()
        
print('Processor()', flush=True)
processor = Processor()
print('Processor() done', flush=True)

time.sleep(10)
for i in range(10):
    processor.put_nowait(i)
    time.sleep(1)
