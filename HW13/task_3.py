import time


class MyCustomException(Exception):
    def __init__(self, message="Custom exception is occurred"):
        self.message = message
        self.name = "Custom Exception"
        super().__init__(self.message)
        cur_time = time.localtime()
        call_time = time.asctime(cur_time)
        with open("exception_info.txt", "w") as file:
            file.write(f"Exception name: {self.name}. Call time: {call_time}")

    def get_error(self):
        return self.message


try:
    raise MyCustomException
except MyCustomException as e:
    print(e)
