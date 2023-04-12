class MyManager:

    def __enter__(self):
        print("==========")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"{exc_type.__name__}: {exc_val}")
        print("==========")
        return True


def example_func():
    print(1 / 0)


with MyManager():
    example_func()
