from contextlib import contextmanager, asynccontextmanager
import asyncio



class Guest:
    def __init__(self) -> None:
        self.status: str | None = None

    def __enter__(self) -> str:
        print('witam')
        self.status = 'gość w dom, Bóg w dom'
        return self.status
    
    def __exit__(self, error: Exception, value: object, traceback: object) -> None:
        print('żegnam')
        self.status = 'gość jest jak ryba'


@contextmanager
def handle_guest():
    try:
        print('witam')
        yield 'gość w dom, Bóg w dom'
    finally:
        print('żegnam')


@asynccontextmanager
async def handle_guest_async():
    print('The guest is comming...')
    await asyncio.sleep(2)
    try:
        print('witam')
        yield 'gość w dom, Bóg w dom'
    finally:
        print('The guest is leaving...')
        await asyncio.sleep(2)
        print('żegnam')


async def main():
    async with handle_guest_async() as status:
        print(status)


if __name__ == "__main__":
    with Guest() as status:
        print(status)
    print()

    with handle_guest() as status:
        print(status)
    print()

    asyncio.run(main())
