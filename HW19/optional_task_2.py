class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        compare_str_1 = self.name.lower()
        compare_str_2 = other.name.lower()
        if compare_str_1 == compare_str_2:
            return True
        else:
            return False


first_user = User("IvAn")
second_user = User("ivan")
print(first_user == second_user)
