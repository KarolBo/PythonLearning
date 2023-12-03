import asyncio
import time

from req_http import get_http, get_http_sync


async def get_pokemon(pokemon_id: int):
    response = await get_http(f'http://pokeapi.co/api/v2/pokemon/{pokemon_id}')
    return response

def get_pokemon_sync(pokemon_id: int):
    response = get_http_sync(f'http://pokeapi.co/api/v2/pokemon/{pokemon_id}')
    return response
            

async def main():
    n = 20

    start = time.time()
    pokemons = await asyncio.gather(*[get_pokemon(i+1) for i in range(n)])
    stop = time.time()
    print(f'Executed in {stop - start} s')

    start = time.time()
    [get_pokemon_sync(i+1) for i in range(n)]
    stop = time.time()
    print(f'Executed in {stop - start} s')

    for pokemon in pokemons:
        print(pokemon['name'])


if __name__ == '__main__':
    asyncio.run(main())