import asyncio
import time
import numpy as np
from wled import WLED

# python-wled docs:
# https://github.com/frenck/python-wled/blob/main/src/wled/wled.py

# this pattern is all off except one bulb, which is red. it moved forward one at a time.
async def main() -> None:
    """Show example on controlling your WLED device."""
    async with WLED("wled-test1.local") as led:
        
        t = 0
        pattern = np.tile(
            np.array([0, 0, 0]),
            (150, 1))

        while True:
            
            print("t = " + str(t))
            pattern[t] = np.array([0, 0, 0])
            pattern[(t + 1) % 150] = np.array([255, 0, 0])

            await led.segment(0, transition = 0, individual = pattern.tolist())

            time.sleep(0.1)
            t = (t + 1) % 150

if __name__ == "__main__":
    asyncio.run(main())