class MyStr:
    def __init__(self, string):

        self.string = string

    def __str__(self):
        new_str = self.string.upper()
        return new_str


user_name = MyStr("Ivan Ivanovich")
print(user_name)
