#!/usr/bin/env python3
"""Module for basic async syntax with wait_random coroutine."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay and return it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
