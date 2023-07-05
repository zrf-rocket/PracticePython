import asyncio

async def say_hello():
    print("hello steverocket")
    await asyncio.sleep(3)
    print("hello cramer")

loop = asyncio.get_event_loop()
loop.run_until_complete(say_hello())

