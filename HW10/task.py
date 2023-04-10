def reverse_range_func(n):
    while n >= 0:
        print(f"{n} ")
        return reverse_range_func(n - 1)


reverse_range_func(10)
