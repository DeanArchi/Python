import time


def info_decorator(times):
    def wrapper(func):
        for _ in range(0, times):
            print(func.__name__)
        cur_time = time.localtime()
        call_time = time.asctime(cur_time)
        print(call_time)

        def inner(*args, **kwargs):
            func(*args, **kwargs)
        return inner
    return wrapper

    # ==== I decided to keep 1 version here:
    # def wrapper(*args, **kwargs):
    #     print(func.__name__)
    #     cur_time = time.localtime()
    #     call_time = time.asctime(cur_time)
    #     print(call_time)
    #     func(*args, **kwargs)
    # return wrapper


@info_decorator(5)
def print_numbers(*args):
    print(args)


@info_decorator(2)
def print_some_info(name, phone):
    print(name, phone)


@info_decorator(3)
def elementary_print():
    print("Hello world")


print_numbers(1, 4, 6, 7)
print_some_info("Ivan", 123)
elementary_print()
