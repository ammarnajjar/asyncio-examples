import pytest

from hello import say


@pytest.mark.asyncio
async def test_hello():
    res = await say('hello', 0)
    assert 'hello' == res
