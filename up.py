import asyncio
import logging


async def co_a():
    logging.warning("Task A start")
    await asyncio.sleep(0)
    logging.warning("Task A stop")


async def co_b():
    logging.warning("Task B start")
    await asyncio.sleep(0)
    logging.warning("Task B stop")


async def cli():
    tasks = [co_a(), co_b()]
    await asyncio.gather(*tasks)


asyncio.run(cli())
