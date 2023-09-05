import asyncio

async def call_foursquare_api():
    print("foursquare call started")
    await asyncio.sleep(2)
    print("foursquare call finished")
    
async def call_spotify_api(): # 3. 
    print("spotify call started")
    await asyncio.sleep(1) #4. 
    print("spotify call finished") # 5. 
    

async def main():
    await asyncio.gather(call_foursquare_api(), call_spotify_api()) # 2. 
    print('done everything')

asyncio.run(main()) # 1. 
