def upper_case(lst):
    new_list = lst.upper()
    return new_list


countries = ["Ukraine", "Poland", "germany", "spAin", "uNiTeD kingdom"]

result = list(map(upper_case, countries))
print(result)
