import asyncio


async def waiter(event):
    print('waiting for it ...')
    await event.wait()
    print('... got it')


async def main():  # pragma no cover
    event = asyncio.Event()
    waiter_task = asyncio.create_task(waiter(event))
    await asyncio.sleep(1)
    event.set()
    await waiter_task


if __name__ == "__main__":  # pragma no cover
    asyncio.run(main())
