import asyncio, time

async def fetch_data(param: str) -> str:
    print(f"starting to fetch {param}...")
    await asyncio.sleep(1)
    print(f"successfully fetched {param}...")
    return f"result of {param}"

async def main():
    result1 = await fetch_data("foo")
    result2 = await fetch_data("bar")
    return [result1, result2]

if __name__ == "__main__":
    t1 = time.perf_counter()
    # create an event loop
    results = asyncio.run(main())
    print(results)
    t2 = time.perf_counter()
    print(f"Finished in {t2-t1:.2f} seconds")

"""
hmm, still 2 seconds...why?

await fetch_data("foo") we are scheduling and running them to completion at the same time. This is same as syncronous code.

starting to fetch foo...
successfully fetched foo...
starting to fetch bar...
successfully fetched bar...
['result of foo', 'result of bar']
Finished in 2.00 seconds
"""