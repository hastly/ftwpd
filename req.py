import logging

import aiohttp
from aiohttp.web_exceptions import HTTPForbidden


async def aiohttp_fetch(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                return response
        except HTTPForbidden:
            logging.error("Rate limit exceed")
