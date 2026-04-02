from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

# Example 1
# Async with blocking code. Bad Practice
@app.get("/1")
async def route1():
    print("{[route1]: hello..}")
    # Blocks the entire event loop. No other requests can run during those 5 seconds
    time.sleep(5)
    print("{[route1]: bye..}")
    
# Example 2
# Async with non-blocking code. Good for Concurrent processing
@app.get("/2")
async def route2():
    print("{[route1]: hello..}")
    # I’m waiting, but others can use the event loop while I pause.
    # Event loop switches to another request
    await asyncio.sleep(5)
    print("{[route1]: bye..}")

# Example 3
# Normal Functions (Default). Good for parallel processing (uses thread)
# Even though this is blocking, FastAPI handles it smartly.
# It does NOT block the event loop
# Each request gets a thread
# Good for blocking I/O or CPU-light blocking tasks
@app.get("/3")
def route3():
    print("{[route1]: hello..}")
    time.sleep(5)
    print("{[route1]: bye..}")

"""
uv pip install uvcorn
uvicorn app:app --reload
"""