# == Using built-in function:
arr = [12, 4, 6, 7, 4, 555, 7, 0, 44, 104, 17]
print(max(arr))


# == Created function by my own:
def my_max(array):
    max_number = 0
    for number in array:
        if number > max_number:
            max_number = number
    return max_number


arr_1 = [12, 4, 6, 7, 4, -2, 7, 0, 44, 104, 17]
print(my_max(arr_1))

# == Using lambda function:
arr_2 = [12, 4, 34657, 7, 4, -2, 12487, 0, 44, 104, 17]
x = lambda array: max(array)
print(x(arr_2))
