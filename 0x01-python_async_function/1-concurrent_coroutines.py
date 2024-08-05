#!/usr/bin/env python3
"""
execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
from 0_basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        # Insert delay in the sorted position
        if not delays or delay >= delays[-1]:
            delays.append(delay)
        else:
            for i in range(len(delays)):
                if delay < delays[i]:
                    delays.insert(i, delay)
                    break
    return delays