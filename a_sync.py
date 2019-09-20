import asyncio
import logging
import random
from time import sleep


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


def run_sync_a_sync():
    logging.info("Sync run")
    sync_run()

    logging.info("A-sync run")
    asyncio.run(a_sync_run())
