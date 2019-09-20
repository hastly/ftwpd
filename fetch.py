import asyncio
import logging
from urllib import request

from lib import Timer
from defs import URL, MAX_CLIENTS
from req import aiohttp_fetch


def fetch_sync(pid):
    logging.info(f"Sync fetch started: #{pid}")
    timer = Timer()
    response = request.urlopen(URL)
    datetime_hdr = response.getheader("Date")

    logging.info(f"Sync fetch #{pid}: {datetime_hdr}, took: {timer.passed():.2f} seconds")

    return datetime_hdr


def run_fetches_sync():
    timer = Timer()
    for pid in range(1, MAX_CLIENTS + 1):
        fetch_sync(pid)
    logging.info(f"Fetch sync process took: {timer.passed()}")


async def fetch_a_sync(pid):
    logging.info(f"A-sync fetch started: #{pid}")
    timer = Timer()
    response = await aiohttp_fetch(URL)
    datetime_hdr = response.headers.get("Date")

    logging.info(f"A-sync fetch #{pid}: {datetime_hdr}, took: {timer.passed():.2f} seconds")
    response.close()

    return datetime_hdr


async def run_fetches_a_sync():
    timer = Timer()
    tasks = [
        fetch_a_sync(pid)
        for pid in range(1, MAX_CLIENTS + 1)
    ]
    await asyncio.wait(tasks)
    logging.info(f"Fetch A-sync process took: {timer.passed()}")
