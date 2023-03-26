import asyncio
from reader import Reader
from util import getUrl, printProgress
from constants import HEADERS

class Scraper(Reader):
    chunksSize = 1000
    requestLimit = 250

    def __init__(self, limiter=None):
        super(limiter)
        #self.startChunk = int(starting) if starting.isnumeric() else 0

    async def getWebsite(self, session, name):
        url = getUrl(name)
        try:
            async with session.get(url, headers=HEADERS) as resp:
                self.fetchDone += 1
                printProgress(self.fetchDone, self.chunksSize, "- Collecting data: ")
                jsonResp = await self.getJson(name, resp)
                return jsonResp
        except asyncio.TimeoutError:
            print(f"Timeout at {name}")
        except:
            print()
            colorPrint("Found error", f"{url}", "fail")
            return [
                name, {
                    "status": 400,
                    "modified": None,
                    "size": None
                    }
            ]