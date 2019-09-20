import asyncio
import logging
from time import time

start = time()


def tic():
    return f"{(time() - start):1.1f}"


async def co_sleeping_a():
    logging.warning(f"Task A start: {tic()}")
    await asyncio.sleep(2)
    logging.warning(f"Task A stop: {tic()}")


async def co_sleeping_b():
    logging.warning(f"Task B start: {tic()}")
    await asyncio.sleep(2)
    logging.warning(f"Task B stop: {tic()}")


async def co_early_bird():
    logging.warning(f"Do stuff: {tic()}")
    await asyncio.sleep(1)
    logging.warning(f"Done, while all others were sleeping: {tic()}")


async def cli():
    tasks = [co_sleeping_a(), co_sleeping_b(), co_early_bird()]
    await asyncio.gather(*tasks)


asyncio.run(cli())
