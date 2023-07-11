#!/usr/bin/env python3
"""
contains a fucntions names measure_runtime that
measure the time it takes for async_comprehension to
run
"""
import time
import asyncio


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ measure the total runtime """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.time() - start
