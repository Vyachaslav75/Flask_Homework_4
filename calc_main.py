import time
import calc_thread
import calc_multiproc
import calc_async

def main():
    start_time = time.time()
    calc_thread.calc_thread()
    print(f"Calced in {time.time() - start_time:.2f} seconds")
    start_time = time.time()
    calc_multiproc.calc_multi()
    print(f"Calced in {time.time() - start_time:.2f} seconds")
    start_time = time.time()
    calc_async.run_async()
    print(f"Calced in {time.time() - start_time:.2f} seconds")
    
if __name__ == '__main__':
    main()