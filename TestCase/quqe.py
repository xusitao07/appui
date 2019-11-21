import asyncio,time
import aiohttp,requests
async def show(num):
    print("num is {}".format(num))
    await asyncio.sleep(1)
    # time.sleep(1)
start = time.time()
print("cost:",start - start)
tasks = [asyncio.ensure_future(show(i))for i in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print("cost:",end - start)
