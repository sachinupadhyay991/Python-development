import asyncio

# Scheduling corouttine at once
async def say(what, when):
    for i in range(len(what)):
        await asyncio.sleep(when)
        print(what)

async def say1(what, when):
    await asyncio.sleep(when)
    print(what)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(say("first",2),say1("second",4)))
loop.close()
