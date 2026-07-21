# await

# The `await` keyword is used to pause the execution of an async function
# until the awaited coroutine completes. Here's an example that demonstrates
# how to use `await` with an asynchronous function:
import asyncio


# defferent use of async and await
async def get_url():
    print("Fetching URL...")
    await asyncio.sleep(2)  # Simulate a network request with a 2-second delay
    print("URL fetched!")


print("Starting the async function...")
asyncio.run(get_url())


# In this example, the `say_hello` function is defined as an asynchronous
# function using the `async def` syntax. Inside the function, we print
# "Hello", then use `await asyncio.sleep(1)` to pause the execution for
# 1 second before printing "World". The `asyncio.run()` function is used
# to run the asynchronous function.

# Note: The `await` keyword can only be used inside an async function.
# If you try to use `await` outside of an async function, you'll get a
# SyntaxError.

# You can also use `await` with other asynchronous functions or coroutines,
# such as those provided by libraries like `aiohttp` for making asynchronous
# HTTP requests or `aiomysql` for interacting with MySQL databases
# asynchronously.
