# async

# Async programming in Python allows you to write concurrent code using the
# `async` and `await` keywords. Here's a simple example:
import asyncio


async def main():
    print("Hello")
    await asyncio.sleep(1)
    wait_for = asyncio.create_task(asyncio.sleep(2))
    await wait_for
    print("World")


asyncio.run(main())

# In this example, the `main` function is defined as an asynchronous function
# using the `async def` syntax. Inside the function, we print "Hello", then
# use `await asyncio.sleep(1)` to pause the execution for 1 second before
# printing "World". The `asyncio.run()` function is used to run the
# asynchronous function.
