import aiohttp


async def aiohttp_fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response
