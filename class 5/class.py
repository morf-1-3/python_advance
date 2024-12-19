# import threading
# import os
# import time

# PATH = os.path.abspath(__file__ + '/..')
# FILE1_PATH = PATH +"/"+"file1.txt"
# FILE2_PATH = PATH + "/file2.txt"
# FILE3_PATH = PATH + "/file3.txt"
# stop_threads = False

# def check_file(name_file:str):
#     while not stop_threads:
#         with open(PATH+"/"+name_file,"r") as f:
#             data = f.read()
#             if(data.upper() == "HELLO"):
#                 print(f"{name_file} is ready")
#             else:
#                 print(f"{name_file} is not ready")
#         time.sleep(0.5)
        
        

# files = ["file1.txt","file2.txt","file3.txt"]
# threads =[]
# for file in files:
#     print(file)
#     thread = threading.Thread(target=check_file,args=(file,))
#     threads.append(thread)
    

# for thread in threads:
#     thread.start()

# a = input()
# stop_threads = True
# print("FINISH")
# time.sleep(30)



import threading
import time

def task(name):
    print(f"Потік {name} почався")
    time.sleep(2)
    print(f"Потік {name} завершився")

threads = []
for i in range(3):
    t = threading.Thread(target=task, args=(f"Task-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()