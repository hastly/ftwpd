import asyncio
import logging

from a_sync import run_sync_a_sync
from completed import fetch_first_completed
from fetch import run_fetches_a_sync, run_fetches_sync
from sleepers import run_sleepers


logging.getLogger().setLevel(logging.INFO)
logging.basicConfig()
logging.info("Started")


async def cli():
    # await run_sleepers()
    # await run_fetches_a_sync()
    await fetch_first_completed()


asyncio.run(cli())
# run_sync_a_sync()
# run_fetches_sync()
