from time import time
import asyncio

async def get_pages(site_name):
    await asyncio.sleep(0.5)
    print(f"Get pages for {site_name}")
    return range(1, 4)


async def get_page_data(site_name, page):
    await asyncio.sleep(1)
    return f"Data from page {page}({site_name})"



async def spider(site_name):
    all_data = []
    pages = await get_pages(site_name)
    for page in pages:
        data = await get_page_data(site_name, page)
        all_data.append(data)
    return all_data


# print(spider("Blog"))
# spider("News")
# spider("Forum")

start = time()

spiders = [
    asyncio.ensure_future(spider("Blog")),
    asyncio.ensure_future(spider("News")),
    asyncio.ensure_future(spider("Forum")),
]

event_loop = asyncio.get_event_loop()
result = event_loop.run_until_complete(spider("API"))
print(result)
event_loop.close()

print("{:.2F}".format(time() - start))