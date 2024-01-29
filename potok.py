import threading
import time
import requests
from pathlib import Path

start_time = time.time

def download(url):
    response = requests.get(url)
    filename = Path(url).name
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")
    
        

def down_thread(urls):
    
    threads = []
    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()
        
        
#url1 = 'https://trikky.ru/wp-content/blogs.dir/1/files/2023/03/23/zyro-image-11.jpg'


if __name__ == '__main__':
    url1 = ['https://trikky.ru/wp-content/blogs.dir/1/files/2023/03/23/zyro-image-11.jpg',
            'https://laplaya-rus.ru/wp-content/uploads/a/6/e/a6e772531f689ca026971dc047e845b3.jpeg',
            'https://www.nastol.com.ua/download.php?img=201612/1680x1050/nastol.com.ua-196885.jpg',
            'https://escapewithprocdn.azureedge.net/pageimages/shutterstock_528933889.jpg',
            'https://zabavdom.ru/wp-content/uploads/1/5/5/15542589a6a047df1583e83b3cf5b385.jpeg',
            'https://i.artfile.ru/3200x1931_714314_[www.ArtFile.ru].jpg',
            'https://1.bp.blogspot.com/-7aR6JVbhftY/VCgocF_ypKI/AAAAAAAAhAA/ZmYHeGta2pA/s1600/21.jpg']
    
    down_thread(url1)