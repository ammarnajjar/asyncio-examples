import asyncio
import time
from typing import Any


async def say_after(delay: int, what: Any) -> None:
    await asyncio.sleep(delay)
    print(what)


async def nested() -> int:
    return 42


async def main() -> None:  # pragma no cover
    print(f'started at {time.strftime(" %X ")}')

    t1 = asyncio.create_task(say_after(2, 'hello'))
    t2 = asyncio.create_task(say_after(1, 'world'))
    t3 = asyncio.create_task(say_after(1, await nested()))

    await asyncio.gather(t1, t2, t3)
    print(f'finished at {time.strftime(" %X ")}')


if __name__ == '__main__':  # pragma no cover
    asyncio.run(main())
