import logging
from urllib import request

from lib import Timer
from defs import URL
from req import aiohttp_fetch


def fetch_sync(pid):
    logging.info("Sync fetch started: #{pid}")
    timer = Timer()
    response = request.urlopen(URL)
    datetime_hdr = response.getheader("Date")

    logging.info(f"Sync fetch #{pid}: {datetime_hdr}, took: {timer.passed():.2f} seconds")

    return datetime_hdr


async def fetch_a_sync(pid):
    logging.info("A-sync fetch started: #{pid}")
    timer = Timer()
    response = await aiohttp_fetch(URL)
    datetime_hdr = response.headers.get("Date")

    logging.info(f"A-sync fetch #{pid}: {datetime_hdr}, took: {timer.passed:.2f} seconds")
    response.close()

    return datetime_hdr
