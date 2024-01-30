#from multiprocessing import Process, Pool
import multiprocessing
import time
from fill_list import fill_list

counter = multiprocessing.Value('i', 0)


def calc_part(part_list, cnt):
    global counter
    res = 0
    #print(len(part_list))
    #print(cnt.value)
    for i in part_list:
        res+=i
    #counter+= res
    with cnt.get_lock():
        cnt.value += res
    

def calc_multi():
    processes = []
    my_list = fill_list()
    my_ind = [(0, 200000), (200001, 400000), (400001, 600000), (600001, 800000), (800001, 999999)]
    for i, j in my_ind:
        process = multiprocessing.Process(target=calc_part, args=(my_list[i:j], counter,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    print(counter.value)
        
if __name__ == '__main__':
    #calc_part(fill_list())
    start_time = time.time()
    calc_multi()
    print(f"Calced in {time.time() - start_time:.2f} seconds")
    #print(counter.value)