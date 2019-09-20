import asyncio

from a_sync import run_sync_a_sync
from sleepers import run_sleepers


async def cli():
    await run_sleepers()


asyncio.run(cli())
run_sync_a_sync()
