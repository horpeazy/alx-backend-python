#!/usr/bin/env python3
"""
Contains a function name async_generator that will
will loop 10 times, each time asynchronously wait 1
second, then yield a random number between 0 and 10
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async generator yields 10 random numbers

    Args:
        None
    Return:
        None
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
