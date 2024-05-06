#!/usr/bin/env python3
"""
This is an asynchronous function

"""

import asyncio
import random


async def wait_random(max_delay=10):
    """ THis is a coroutine async function """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return (random_delay)
