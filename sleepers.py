import asyncio
import logging

from lib import Timer


async def co_sleeping_a(timer):
    logging.warning(f"Task A start: {timer.tic()}")
    await asyncio.sleep(2)
    logging.warning(f"Task A stop: {timer.tic()}")


async def co_sleeping_b(timer):
    logging.warning(f"Task B start: {timer.tic()}")
    await asyncio.sleep(2)
    logging.warning(f"Task B stop: {timer.tic()}")


async def co_early_bird(timer):
    logging.warning(f"Do stuff: {timer.tic()}")
    await asyncio.sleep(1)
    logging.warning(f"Done, while all others were sleeping: {timer.tic()}")


async def run_sleepers():
    timer = Timer()
    tasks = [fn(timer) for fn in [co_sleeping_a, co_sleeping_b, co_early_bird]]
    await asyncio.gather(*tasks)
