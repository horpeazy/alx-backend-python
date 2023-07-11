#!/usr/bin/env python3
"""
contains a function async_comprehension that will
will collect 10 random numbers using an async
comprehensing over async_generator, then return
the 10 random numbers.
"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    async_comprehension returns items from an async generator

    Args:
        None
    Return:
        List of integers
    """
    return [i async for i in async_generator()]
