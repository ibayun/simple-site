import aiohttp
import asyncio
from time import time


def write_data(data):
    filename = './async_picrures/{}.ipeg'.format(int(time() * 1000))
    with open(filename, 'wb') as f:
        f.write(data)


async def fetch_data(url, session):
    async with session.get(url,  allow_redirects=True) as resp:
        data = await resp.read()
        # name = url.split('/')[-3]
        # print(name)
        write_data(data)


async def main():
    url = "https://picsum.photos/400/300"
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(82):
            task = asyncio.ensure_future(fetch_data(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    # asyncio.run(main())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    print('Done!')
