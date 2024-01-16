#!/usr/bin/env python3
''' Task: A coroutine called async_generator that takes no
                 arguments.
                 The coroutine will loop 10 times, each time asynchronously
                 wait 1 second, then yield a random number between 0 and 10.
                 Use the random module.
'''

import asyncio
import random

async def async_generator():
    ''' Generator that yields a random value between 0 and 10 every second,
        10 times. '''
    n: int = 0
    while n < 10:
        n += 1
        await asyncio.sleep(1)
        yield random.uniform(0, 10)