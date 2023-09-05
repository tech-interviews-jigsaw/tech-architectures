import asyncio


async def main(player_number):
    for i in range(5):
        print(f'MC against player {player_number} for move {i}')
        await asyncio.sleep(1)
        print(f'{player_number} for move {i}')


async def run_it():
    await asyncio.gather(main('mortal 1'), main('mortal 2'), main('mortal 3'))

asyncio.run(run_it())


