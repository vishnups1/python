"""
In previous examples we have been creating tasks one at a time and awaiting them manually.

But a lot of time we want to create a buch of tasks and run them all at once we can do it using below options.

- gather coroutines
- gather tasks
- task groups
"""

import asyncio

async def fetch_data(param: str, delay: int):
    print(f"fetching {param}...")
    await asyncio.sleep(delay)
    print(f"completed fetching {param}...")

async def main():
    ###################
    # Gather Coroutines
    ###################

    # coroutines = [fetch_data(v[0], v[1]) for _, v in enumerate([("foo", 5), ("bar", 10)])]
    # # * Unpack or Splat operator
    # results = await asyncio.gather(*coroutines, return_exceptions=True)
    # print(results)

    ###############
    # Gather Tasks
    ###############

    # tasks = [asyncio.create_task(fetch_data(v[0], v[1])) for _, v in enumerate([("foo", 5), ("bar", 10)])]
    # results = await asyncio.gather(*tasks, return_exceptions=True)
    # print(results)

    #############
    # Task Group
    #############

    results = []
    async with asyncio.TaskGroup() as tg:
        results.append(tg.create_task(fetch_data("foo", 5)))
        results.append(tg.create_task(fetch_data("bar", 15)))
        # all tasks are awaited when the context manager exits

    print([result.result() for result in results])

"""
The key difference between gather and task groups is how they handle errors.

If you use asyncio.gather() with default "return_exceptions=False" (which is not recommended). With False if one task fails,
then it raises the first exception that it saw, you don't get a bundle of errors or any of the successful tasks. If it fails other tasks won't be cancelled.
You will have a risk of having orphaned tasks.

Task groups also fails quickly but it gives better errors and handle cleanups.

When to use Gather and Task Groups?

If you want tasks to continue running even if some failed then you will use gather with return_exceptions=True.

If you want all of the tasks fail together or succeed together then you will need to use a task group.
"""


if __name__ == "__main__":
    asyncio.run(main())