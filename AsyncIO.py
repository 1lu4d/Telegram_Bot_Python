import asyncio

async def sendmeal(message:int):
    print("beninging senging mail")
    await asyncio.sleep(1) # stops EVERYTHING and waits 3 secs
    print(f"meil sent: {message}")
#for k in range(10):
    #asyncio.run(sendmeal(k)) # BAD
#   ^   ^   ^   ^
#   |   |   |   | --> this code is actually sync and not async
#   |   |   |   |
async def main():
    tasks = [sendmeal(i) for i in range(10)]
    await asyncio.gather(*tasks) # .gather is the only way to run things simultaneously
asyncio.run(main())