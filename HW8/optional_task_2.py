# 1 option
def check(check_lst):
    if type(check_lst) is int:
        return True
    else:
        return False


lst = [1, 2, 3, "1", "2", "3", "Hello", 5, "(1, 2, 3)", 15, 0, "10", "11", "12", "asd"]
result = list(filter(check, lst))
print(result)


# 2 option


def another_check(check_lst):
    if check_lst.isdigit():
        return True
    else:
        return False


lst1 = ["1", "2", "dfg24", "Hello", "22", "World", "5432", "qwerty12345"]
result1 = list(filter(another_check, lst1))
print(result1)
