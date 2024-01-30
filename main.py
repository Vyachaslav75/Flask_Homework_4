import potok
import multiproc
import async_d
import time
import sys


def main(urls):
    
    start_thr = time.time()
    potok.down_thread(urls)
    print(f"Threads downloads in {time.time() - start_thr:.2f} seconds")
    start_thr1 = time.time()
    multiproc.down_multi(urls)
    print(f"Multiprocess downloads in {time.time() - start_thr1:.2f} seconds")
    start_thr2 = time.time()
    async_d.run_async(urls)
    print(f"Async downloads in {time.time() - start_thr2:.2f} seconds")
    
if __name__ == '__main__':
    if len (sys.argv) > 1:
        urls = []
        for param in sys.argv[1:]:
            urls.append(param)
    else:
        urls = ['https://trikky.ru/wp-content/blogs.dir/1/files/2023/03/23/zyro-image-11.jpg',
            'https://laplaya-rus.ru/wp-content/uploads/a/6/e/a6e772531f689ca026971dc047e845b3.jpeg',
            'https://www.nastol.com.ua/download.php?img=201612/1680x1050/nastol.com.ua-196885.jpg',
            'https://escapewithprocdn.azureedge.net/pageimages/shutterstock_528933889.jpg',
            'https://zabavdom.ru/wp-content/uploads/1/5/5/15542589a6a047df1583e83b3cf5b385.jpeg',
            'https://i.artfile.ru/3200x1931_714314_[www.ArtFile.ru].jpg',
            'https://1.bp.blogspot.com/-7aR6JVbhftY/VCgocF_ypKI/AAAAAAAAhAA/ZmYHeGta2pA/s1600/21.jpg']
    main(urls)

