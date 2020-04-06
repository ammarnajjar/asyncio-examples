import pytest

from factorial import factorial


@pytest.mark.asyncio
async def test_factorial():
    assert 6 == await factorial('', 3)
    assert 24 == await factorial('', 4)
