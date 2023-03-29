# ===== 1. Написати функцію, яка повертає тільки однакові елементи двох множин.
# First option
def same_elements(first_set, second_set):
    res = set()
    for item in first_set:
        for element in second_set:
            if item == element:
                res.add(item)
                continue
    if res:
        return res
    else:
        return "There's no same elements in these 2 sets"


set1 = {1, 2, 3, 5, 7, 9}
set2 = {0, 1, 2, 3, 4, 7, 10}

set3 = {1, 3, 5, 7, 9}
set4 = {2, 4, 6, 8, 10}

result = same_elements(set1, set2)
result1 = same_elements(set3, set4)
print(result)
print(result1)

# Second option. I decided to try built-in function intersection()
res1 = set1.intersection(set2)
res2 = set3.intersection(set4)
print(res1)
print(res2)

# ===== 2. Написати функцію, яка повертає тільки унікальні елементи двох множин.
# First option


def unique_elements(first_set, second_set):
    res = set()
    for item in first_set:
        if item in second_set:
            continue
        else:
            res.add(item)

    for item in second_set:
        if item in first_set:
            continue
        else:
            res.add(item)

    if res:
        return res
    else:
        return "In these 2 sets all elements are the same"


set5 = {0, 1, 2, 3, 4}
set6 = {1, 2, 4, 5, 6}

set7 = {10, 11, 12}
set8 = {10, 11, 12}

res_unique = unique_elements(set5, set6)
res_unique1 = unique_elements(set7, set8)
print(res_unique)
print(res_unique1)

# Second option. I also decided to try built-in function symmetric_difference()
unique_result = set5.symmetric_difference(set6)
unique_result1 = set7.symmetric_difference(set8)
print(unique_result)
print(unique_result1)
