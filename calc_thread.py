import threading
import time
from fill_list import fill_list

counter = 0
start_time = time.time()

def calc_part(part_list):
    global counter
    res = 0
    for i in part_list:
        res+=i
    counter+= res
     

def calc_thread():
    threads = []
    my_list = fill_list()
    my_ind = [(0, 200000), (200001, 400000), (400001, 600000), (600001, 800000), (800001, 999999)]
    for i, j in my_ind:
        thread = threading.Thread(target=calc_part, args=[my_list[i:j]])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(counter)
    
   
if __name__ == '__main__':
    #calc_part(fill_list())
    calc_thread()
    print(f"Calced in {time.time() - start_time:.2f} seconds")
    #print(counter)
