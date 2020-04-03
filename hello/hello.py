import asyncio


async def print_task(task):
    print(await task)


async def say(what, when):
    await asyncio.sleep(when)
    return(what)


async def stop_after(loop, when):
    await asyncio.sleep(when)
    loop.stop()

loop = asyncio.get_event_loop()

loop.create_task(print_task(say('hello', 2)))
loop.create_task(print_task(say('world', 1)))
loop.create_task(stop_after(loop, 3))

loop.run_forever()
loop.close()
