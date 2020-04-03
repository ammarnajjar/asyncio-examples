import asyncio


async def print_every_minute():
    for i in range(10):
        await asyncio.sleep(60)
        print(i, 'minute')


async def print_every_second():
    for i in range(10 * 60):
        for i in range(60):
            print(i, 's')
            await asyncio.sleep(1)


if __name__ == '__main__':  # pragma no cover
    loop = asyncio.get_event_loop()

    loop.run_until_complete(
        asyncio.gather(
            print_every_minute(),
            print_every_second(),
        ),
    )
    loop.close()
