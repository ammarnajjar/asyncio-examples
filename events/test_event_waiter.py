import asyncio
import time

import pytest
from event_waiter import waiter


@pytest.mark.asyncio
async def test_waiter():
    event = asyncio.Event()
    start = time.time()
    waiter_task = asyncio.create_task(waiter(event))
    await asyncio.sleep(1)
    event.set()
    await waiter_task
    end = time.time()
    assert int(end - start) == 1
