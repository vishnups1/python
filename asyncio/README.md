## Concurrency

With synchronous code execution happens one thing after an other. Async doesn't means faster.

We can do other useful work instead of sitting idle while waiting for network requests, database queries etc. That's why asyncio excels at IO bound tasks, which means at any time if your program is waiting for something external it does other stuffs which are waiting to be executed.

Async IO is single threaded and runs on a single process. It uses what's called cooperative multi tasking where task voluntarily gives up control.

For CPU bound taks that needs heavy computation you need processed instead.
