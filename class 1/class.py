import random

def decorator(function):
    def wrapper(*args, **kwargs):
        print("-----------------")
        function(*args,*kwargs)
        print("-----------------")
    return wrapper



@decorator
def print_hello():
    print("HEllo")

@decorator
def squad(a:int):
    print(a**2)

@decorator
def random_num():
    print(random.randint(0,10))

squad(4)
random_num()
print_hello()