import pytest

from gather import nested
from gather import say_after


@pytest.mark.asyncio
async def test_nested():
    assert await nested() == 42


@pytest.mark.asyncio
async def test_say_after(capsys):
    test_string = 'ATest'
    await say_after(0, test_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == test_string
