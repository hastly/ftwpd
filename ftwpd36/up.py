import asyncio
import logging
from asyncio import FIRST_COMPLETED
from collections import namedtuple
from time import time

import aiohttp


logging.getLogger().setLevel(logging.INFO)
logging.info("!")


Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query'),
)


async def http_get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_ip(service):
    start = time()
    logging.info(f"Fetching IP from: {service.name}")

    json_response = await http_get(service.url)
    ip = json_response[service.ip_attr]

    return f"{service.name} finished with result: {ip}, took {(time() - start):.2f} seconds"


async def cli():
    futures = [fetch_ip(service) for service in SERVICES]
    done, pending = await asyncio.wait(
        futures,
        return_when=FIRST_COMPLETED,
    )
    logging.info(done.pop().result())


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(cli())
ioloop.close()
