import asyncio
import aiohttp
import time
from pathlib import Path

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.content.read()
            #content = await response.content() #.text()
            #filename = 'asyncio_' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
            #with open(filename, "w", encoding='utf-8') as f:
            #    f.write(text)
            filename = Path(url).name
            with open(filename, 'wb') as f:
                f.write(content)
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")
            
async def main(urls):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
        await asyncio.gather(*tasks)
        

def run_async(urls):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls))
        
start_time = time.time()

if __name__ == '__main__':
    url1 = ['https://trikky.ru/wp-content/blogs.dir/1/files/2023/03/23/zyro-image-11.jpg',
            'https://laplaya-rus.ru/wp-content/uploads/a/6/e/a6e772531f689ca026971dc047e845b3.jpeg',
            'https://www.nastol.com.ua/download.php?img=201612/1680x1050/nastol.com.ua-196885.jpg',
            'https://escapewithprocdn.azureedge.net/pageimages/shutterstock_528933889.jpg',
            'https://zabavdom.ru/wp-content/uploads/1/5/5/15542589a6a047df1583e83b3cf5b385.jpeg',
            'https://i.artfile.ru/3200x1931_714314_[www.ArtFile.ru].jpg',
            'https://1.bp.blogspot.com/-7aR6JVbhftY/VCgocF_ypKI/AAAAAAAAhAA/ZmYHeGta2pA/s1600/21.jpg']
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(main(url1))
    run_async(url1)