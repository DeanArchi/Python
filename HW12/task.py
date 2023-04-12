import time


def info_decorator(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        cur_time = time.localtime()
        call_time = time.asctime(cur_time)
        print(call_time)
        func(*args, **kwargs)
    return wrapper


@info_decorator
def print_numbers(*args):
    print(args)


@info_decorator
def print_some_info(name, phone):
    print(name, phone)


@info_decorator
def elementary_print():
    print("Hello world")


print_numbers(1, 4, 6, 7)
print_some_info("Ivan", 123)
elementary_print()
