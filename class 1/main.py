# #Exercise 2
# import time
# from functools import lru_cache

# def count_time(function):
#     def wrapper(*args, **kwargs):
#         time_begin = time.time()
#         function(*args, **kwargs)
#         time_rezult =   time.time() - time_begin
#         print("********"*10)
#         return time_rezult
#     return wrapper


# @count_time
# def print_fibonachi(lenght, num1=0, num2=1):
#     for _ in range(lenght):
#         print(num2)
#         num1,num2 = num2,num1+num2

# @count_time
# @lru_cache
# def print_fibonachi1(lenght, num1=0, num2=1):
#     for _ in range(lenght):
#         print(num2)
#         num1,num2 = num2,num1+num2

# @count_time
# @lru_cache(10)
# def print_fibonachi2(lenght, num1=0, num2=1):
#     for _ in range(lenght):
#         print(num2)
#         num1,num2 = num2,num1+num2

# @count_time
# @lru_cache(16)
# def print_fibonachi3(lenght, num1=0, num2=1):
#     for _ in range(lenght):
#         print(num2)
#         num1,num2 = num2,num1+num2



# print(print_fibonachi(25))
# print(print_fibonachi1(25))
# print(print_fibonachi2(25))
# print(print_fibonachi3(25))





# #Exercise 5
# my_list = [4,6,215,7,136,86,1236,967,13,7569,8,315,97,35,98,64,11,46]
# result = map(lambda x: x**2, filter(lambda x : x % 2 ==0 , my_list))


# print(list(result))


# #Exercise 6
# def evennumber(function):
#     result = []
#     def wrapper(lenght:int):
#         for i in function(lenght):
#             if i % 2 == 0:
#                 result.append(i)
#         return result
#     return wrapper

# @evennumber
# def fibonachi(lenght:int):
#     num1=0
#     num2=1
#     for _ in range(lenght,0,-1):
#         num1,num2 = num2,num1+num2
#         yield num1
    
# for i in fibonachi(20):
#     print(i)

# #exercise 7
# from functools import partial

# def multi(num1:int, num2:int):
#     return num1*num2

# func = partial(multi,num1 = 5)
# print(func(num1=6, num2=6))
# print(func(num2=6))
