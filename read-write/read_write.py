import asyncio


async def readbytes(name: str, number: int) -> None:
    with open(name, 'rb') as fi:
        s = fi.read(number)
        await asyncio.sleep(number)
        print(f' File contents: {s!r}')


async def writebytes(name: str, number: int, string: str) -> None:
    with open(name, 'w') as fo:
        fo.write(string)
        await asyncio.sleep(number)
        print(f'Wrote: {string}')


async def main():
    await asyncio.gather(
        readbytes('/dev/urandom', 2),
        readbytes('/dev/random', 3),
        readbytes('/dev/zero', 4),
        writebytes('/tmp/spam', 2, 'spam'),
        writebytes('/tmp/egg', 3, 'egg'),
        writebytes('/tmp/bar', 4, 'bar'),
    )


if __name__ == '__main__':
    asyncio.run(main())
