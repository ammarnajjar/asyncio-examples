import asyncio


async def factorial(name: str, number: int) -> int:
    f = 1
    for i in range(2, number + 1):
        print(f'task {name}: compute factorial({i})...')
        await asyncio.sleep(1)
        f *= i
    print(f'task {name}: factorial({i}) = {f}')
    return f


async def main():  # pragma no cover
    await asyncio.gather(
        factorial('A', 2),
        factorial('B', 3),
        factorial('C', 4),
    )


if __name__ == '__main__':  # pragma no cover
    asyncio.run(main())
