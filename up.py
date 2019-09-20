import asyncio
import logging
import random
from time import time, sleep

start = time()


def tic():
    return f"{(time() - start):1.1f}"


def sync_task(pid):
    sleep(random.randint(0, 2) * 0.0_0_1)
    logging.error(f"Sync task done: #{pid}")


def sync_run():
    for i in range(1, 10):
        sync_task(i)


async def async_task(pid):
    await asyncio.sleep(random.randint(0, 2) * 0.0_0_1)
    logging.error(f"A-sync task done: #{pid}")


async def a_sync_run():
    tasks = [async_task(i) for i in range(1, 10)]
    await asyncio.gather(*tasks)


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


logging.info("Sync run")
sync_run()

logging.info("A-sync run")
asyncio.run(a_sync_run())

asyncio.run(cli())
