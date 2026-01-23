"""
Same as example3 and but changed the order foo -> then -> bar
"""

import asyncio, time

async def fetch_data(param: str, time: int) -> str:
    print(f"starting to fetch {param}...")
    await asyncio.sleep(time)
    print(f"successfully fetched {param}...")
    return f"result of {param}"

async def main():

    """
    Below commented snippet is not concurrent.
    task1 = await asyncio.create_task(fetch_data("foo", 3)): Creates task and awaited immediately
    """

    # task1 = await asyncio.create_task(fetch_data("foo", 3))
    # task2 = await asyncio.create_task(fetch_data("bar", 1))

    foo = asyncio.create_task(fetch_data("foo", 3)) # Scheduled ahead of time
    bar = asyncio.create_task(fetch_data("bar", 1)) # Scheduled ahead of time

    result1 = await foo # Wait until task1 finishes. task1 runs for 3 seconds it get's blocked so the event loop will execute the next scheduled task task2
    print("completed task1")
    result2 = await bar # Wait until task2 finishes
    print("completed task2")

    # Note: Whatever that's gonna awaited is not going to be run. Event loop is going to run whatever is ready and it uses a FIFO queue

    return [result1, result2]

if __name__ == "__main__":
    t1 = time.perf_counter()
    # create an event loop
    results = asyncio.run(main())
    print(results)
    t2 = time.perf_counter()
    print(f"Finished in {t2-t1:.2f} seconds")

"""
starting to fetch foo...
starting to fetch bar...
successfully fetched bar...
successfully fetched foo...
completed task1
completed task2
['result of foo', 'result of bar']
Finished in 3.00 seconds
"""