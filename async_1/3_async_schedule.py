from time import time
import asyncio

def loader(url):
    print(f"Load {url}")



start = time()
async def spider(site_name):
    for page in range(1, 4):
        await asyncio.sleep(1)
        print(site_name, page)


# print(spider("Blog"))
# spider("News")
# spider("Forum")

spiders = [
    asyncio.ensure_future(spider("Blog")),
    asyncio.ensure_future(spider("News")),
    asyncio.ensure_future(spider("Forum")),
]

event_loop = asyncio.get_event_loop()
event_loop.call_soon(loader, "url1") #callback
event_loop.call_later(2.0, loader, "url2")
event_loop.run_until_complete(asyncio.gather(*spiders))
event_loop.close()

print(f"{time() - start:.2F}")