import asyncio
from typing import AsyncGenerator

from async_await import get_pokemon

async def get_next_pokemon() -> AsyncGenerator[str, None]:
    pokemon_id: int = 1
    while True:
        try:
            pokemon = await get_pokemon(pokemon_id)
        except:
            return
        pokemon_id += 1
        yield pokemon['name']

async def main() -> None:
    async for pokemon_name in get_next_pokemon():
        print(pokemon_name)


if __name__ == '__main__':
    asyncio.run(main())