import time


def save_info_decorator(func):
    def wrapper(*args, **kwargs):
        name = func.__name__
        cur_time = time.localtime()
        call_time = time.asctime(cur_time)
        with open("decorator_info.txt", "a") as file:
            file.write(f"Function name: {name}. Function call time: {call_time}\n")
        print(call_time)
        func(*args, **kwargs)
    return wrapper


@save_info_decorator
def print_hello(name):
    print(f"Hello, {name}!")


@save_info_decorator
def sum_numbers(a, b):
    print(a + b)


@save_info_decorator
def print_numbers(*args):
    print(args)


print_hello("Ivan")
sum_numbers(2, 3)
print_numbers(1, 2, 3, 4, 5)
