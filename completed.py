import asyncio
import logging
import random

from defs import URL, MAX_CLIENTS
from lib import Timer
from req import aiohttp_fetch


async def fetch_a_sync(pid):
    timer = Timer()
    sleepy_time = random.randint(2, 5)

    logging.error(
        f"START 1st completed fetch "
        f"{pid}, sleep {sleepy_time} secs."
    )

    await asyncio.sleep(sleepy_time)
    response = await aiohttp_fetch(URL)
    datetime_hdr = response.headers.get("Date")
    response.close()

    logging.error(
        f"FIN 1st Completed fetch {pid} | "
        f"{datetime_hdr}, took {timer.passed():.2f}"
    )


async def fetch_first_completed():
    timer = Timer()
    futures = [fetch_a_sync(pid) for pid in range(1, MAX_CLIENTS + 1)]
    for idx, future in enumerate(asyncio.as_completed(futures)):
        result = await future
        logging.error(f"PROCESS 1st completed fetch took {timer.passed()}")
