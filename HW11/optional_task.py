class MyCustomException(Exception):
    def __init__(self, message="Custom exception is occurred"):
        self.message = message
        super().__init__(self.message)

    def get_error(self):
        return self.message


try:
    raise MyCustomException
except MyCustomException as e:
    print(e)
