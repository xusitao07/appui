import asyncio
import datetime

async def tool():
    asyncio.sleep(1)
    print(5+6)

async def tool2():
    asyncio.sleep(1)
    print(5*6)

async def tool3():
    asyncio.sleep(1)
    print(5**2)

async def tool4():
    asyncio.sleep(1)
    print(6+9)

async def tool5():
    asyncio.sleep(1)
    print(5555)

async def hello():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    await tool()
    await tool2()
    await tool3()
    await tool4()
    await tool5()
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()