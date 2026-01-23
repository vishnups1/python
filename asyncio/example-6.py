"""
If we have some blocking synchronous code that doesn't have some async IO alternative. Then we can use asyncio to pass this off to threads or processes,
the event loop will manage those threads and processes for us.
"""

import asyncio, time

from concurrent.futures import ProcessPoolExecutor

# Converted this to non-async function
def fetch_data(param: str, t: int) -> str:
    print(f"starting to fetch {param}...", flush=True)
    # await asyncio.sleep(time)
    time.sleep(t)
    print(f"successfully fetched {param}...", flush=True)
    return f"result of {param}"

async def main():
    ########################################################################
    # Run in threads
    # Instead of multiplexing in same thread, it creates different threads
    ########################################################################
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data, "foo", 10))
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data, "bar", 15))
    result1 = await task1
    print("task1 completed!")
    result2 = await task2
    print("task2 completed!")

    """
    → ps -M 87471
      USER   PID   TT      %CPU STAT PRI   STIME     UTIME   COMMAND
      v01    87471 s004    0.0  S    31T   0:00.02   0:00.04 /Users/v01/.pyenv/versions/3.12.11/bin/python example-6.py
             87471         0.0  S    31T   0:00.00   0:00.00 
             87471         0.0  S    31T   0:00.00   0:00.00 
    """

    ########################################################################
    # Run in processes
    # Instead of multiplexing in same thread, it creates different processes
    ########################################################################

    # loop = asyncio.get_running_loop()
    
    # with ProcessPoolExecutor() as executor:
    #     task1 = loop.run_in_executor(executor, fetch_data, "foo", 15)
    #     task2 = loop.run_in_executor(executor, fetch_data, "bar", 20)
    #     result1 = await task1
    #     print("task1 completed!")
    #     result2 = await task2
    #     print("task2 completed!")

if __name__ == "__main__":
    t1 = time.perf_counter()
    asyncio.run(main())
    totaltime = (time.perf_counter() - t1)
    print(f"completed in {totaltime}")