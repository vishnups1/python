import asyncio
import time

def sync_function(test_param: str) -> str:
    print("This is a Synchronous function")
    time.sleep(5)
    return f"Sync result: {test_param}"

# also known as co-routine
async def async_function(test_param: str) -> str:
    print("This is a Asynchronous function")
    await asyncio.sleep(5)
    return f"Sync result: {test_param}"

async def main():
    # sync_result = sync_function("helloworld!")
    # print(sync_result)

    """
    1. What are awaitables?

    Awaitables are objects that implement a special __await__() method under the hood.
    The object has to be awaitable to use the keyword 'await' on it

    2. Why can't we await a synchronous function like 'time.sleep()'?

    Synchronous libraries don't have a mechanism to work with the event loop, they don't know how yield control over and resume later.
    __await__() hold the logic to pause the execution and resume later.

    3. What does await do?

    When you await something you are basically telling the event loop to pause the execution of the current function and yield control back to the event loop,
    which can then run an other task and it will stay suspended until the awaitable completes.

    4. Types are awaitable objects in python asyncio
      - Coroutines - Functions defined with "async def" keyword
      - Tasks (Wrappers around Coroutines)
      - Futures (Low level objects representing eventual results)

      We don't use Futures directly in python we write courotines and we schedule them as tasks and asyncio uses futures under the hood to track those results
    """

    ############
    # Coroutine
    ############
    # coroutine_obj = async_function("helloworld!")
    # result = await coroutine_obj
    # print(result)

    """
    When we await an coroutine object direcly like above it's both scheduled on event loop and run to completion at the same time
    """

    #######
    # Task
    #######

    task = asyncio.create_task(async_function("helloworld"))
    task_result = await task
    print(task_result)

    """
    Tasks are wrapped coroutines that can be executed independently. Tasks are how we actually run coroutines concurrently.

    When you wrap a couroutine under a task asyncio.create_task() it's handed over to event loop and scheduled to run whenever it gets a chance.
    
    Task will keep track of whether the coroutine finished successfully, raise an error or got cancelled just like future. Infact tasks are futures under the hood,
    with extra logic to run the courotine to do the work.

    Unlike couroutine object tasks can be scheduled on the event loop and sit there without being run until the loop gets control. You can queue up multipe tasks at once,
    and event loop can run whenever it's ready.
    """

if __name__ == "__main__":
    """
    To run an async function we need an event loop.
    
    asynio.run() creates an event loop and main() returns a coroutine
    
    Event loop is the actual engine that runs and manages the asyncronous functions. Think of it as a scheduler.
    This keeps track of all tasks when a task is suspended because the task waiting for something else then the control returns to the eventloop
    which then finds an other task to execute. 
    """
    asyncio.run(main())