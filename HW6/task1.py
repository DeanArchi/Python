# == Task 1

def power_of_number(number, number_pow):
    return number ** number_pow


user_number = int(input("write here number: "))
user_pow = int(input(f"Write here power of number '{user_number}': "))
value = power_of_number(user_number, user_pow)
print(f"{user_number} ** {user_pow} = {value}")

# == Task 2


def sum_numbers(*args):
    result = 0
    for arg in args:
        result += arg
    return result


print(sum_numbers(2, 4, 6, 8, 10))
print(sum_numbers(1, 3, 5, 7, 9, 11, 13))

