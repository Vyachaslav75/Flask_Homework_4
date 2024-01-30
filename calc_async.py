import asyncio
import time
from fill_list import fill_list

counter = 0
start_time = time.time()

async def calc_part(part_list):
    global counter
    res = 0
    for i in part_list:
        res+=i
    #print(res)
    counter+= res
    
    

async def main():
    tasks = []
    my_list = fill_list()
    my_ind = [(0, 200000), (200001, 400000), (400001, 600000), (600001, 800000), (800001, 999999)]
    for i, j in my_ind:
        #print(len(my_list[i:j]))
        task = asyncio.ensure_future(calc_part(my_list[i:j]))
        tasks.append(task)
        await asyncio.gather(*tasks)
        

def run_async():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(counter)
    
if __name__ == '__main__':
    run_async()
    print(f"Calced in {time.time() - start_time:.2f} seconds")
    #print(counter)