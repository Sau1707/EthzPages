import aiohttp
import asyncio
from src.util import Reader, printProgress, getUrl

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

'''
users = Reader("ethz_names.txt")
print(len(users))
for i, user in enumerate(users):
    async with aiohttp.ClientSession() as session:
    print(i, ")", user)
'''

async def getWebsite(i, session, url):
    global done, users

    async with session.get(url) as resp:
        done += 1
        printProgress(done, len(users), "Collecting data")
        return resp
    
async def main():
    global loop
    
    try:
        async with aiohttp.ClientSession() as session:
            tasks = []
            tot = len(users) - 1
            for i, user in enumerate(users):
                printProgress(i, tot, prefix="Setting up tasks:")
                url = getUrl(user)
                tasks.append(asyncio.ensure_future(getWebsite(i, session, url)))
            print('Beginning data collection...')
            finisched_tasks = await asyncio.gather(*tasks)
            for task in finisched_tasks:
                print(task.status, task.headers["Last-Modified"])

    except KeyboardInterrupt:
        total = len(tasks) - 1 
        for i, t in enumerate(tasks):
            printProgress(i, total, prefix="Cancelling tasks")
            t.cancel()
        return

if __name__ == '__main__':
    done = 0
    users = Reader("ethz_names.txt", 100)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print()
        print('Cancelling...')
