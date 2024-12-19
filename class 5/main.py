# import threading
# from concurrent.futures import ThreadPoolExecutor
# import time
# import sys
# sys.set_int_max_str_digits(100000)

# def count_fuctorial(n:int,name:str):
    
#     sum = 1
#     for i in range(1,n):
#         sum = sum * i
#     print(f"FINISH {name}")
#     return sum
# threads = []
# thread1 = threading.Thread(target=count_fuctorial,args=(100000,"thread1"))
# thread2 = threading.Thread(target=count_fuctorial,args=(100000,"thread1"))
# thread3 = threading.Thread(target=count_fuctorial,args=(100000,"thread1"))
# thread4 = threading.Thread(target=count_fuctorial,args=(100000,"thread1"))
# threads.append(thread1)
# threads.append(thread2)
# threads.append(thread3)
# threads.append(thread4)
# start_time = time.time()
# # for thread in threads:
# #     thread.start()
# # for thread in threads:
# #     thread.join()
# # print(time.time()-start_time)
# # print("wos threads")

# # start_time = time.time()
# # count_fuctorial(100000,"1")
# # count_fuctorial(100000,"2")
# # count_fuctorial(100000,"3")
# # count_fuctorial(100000,"4")
# # print(time.time()-start_time)
# # print("wos without threads")
# print("gp")

# start_time = time.time()
# with ThreadPoolExecutor(max_workers=3) as executor:
#     # Виконання завдань
#     futures = [executor.submit(count_fuctorial, 100000,f"pool{i}") for i in range(5)]

#     for future in futures:
#         future.result()
# print(time.time()-start_time)
# print("wos without threads")


#EXERCISE 2

import threading
import time
import os

PATH = os.path.abspath(__file__+"/..")  + "/" + "file.txt"
print(PATH)


def check_file(path:str):
    stop_thread = False
    print("start check")
    while not stop_thread:
        try:
            with open(PATH,"r") as f:
                data = f.read()
        except FileNotFoundError:
            print("File not exists")
            time.sleep(5)  
            continue      
        
        if data == "Wow!":
            file_delete.set()
            stop_thread = True
        else:
            print("not Wow!")
            time.sleep(5)

def delete_file(path:str):
    print("wait event")
    file_delete.wait()
    os.remove(path)
    print("File delete")





file_delete = threading.Event()

thread1 = threading.Thread(target=check_file,args=(PATH,))
thread2 = threading.Thread(target=delete_file,args=(PATH,))
thread1.start()
thread2.start()