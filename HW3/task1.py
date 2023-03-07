
# 1. Використовуючи функцію print, надрукувати фразу “I love Python” 42 рази.
# Оскільки цикли ще не розглядали - буде так:)
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")
print("I love Python")

# 2. Створити змінну age_in_month, надавши їй значення вашого поточного віку в місяцях.
age_in_month = 18 * 12 + 5
print(f"My age in months: {age_in_month}")

# 3. Створити змінну age_in_years, в яку записати ваш вік в роках на основі попередньої змінної.
age_in_years = int(age_in_month / 12)
print(f"My age in years: {age_in_years}")

# 4. Створити змінну my_age, яка буде містити рядок “Му name is … I’m … years old”, де на замість
# пропусків буде підставлятись ваші імʼя та вік. Значення віку слід брати зі змінної age_in_years.
my_name = "Ivan"
my_age = f"My name is {my_name}. I'm {age_in_years} years old"
print(my_age)

# 5. Створити змінну зі значенням 1. Використовуючи оператори порівняння, порівняти її із
# будь-якими іншими значеннями (мінімум 5 порівнянь) і перевірити вивід в інтерпретаторі.
compare = 1

print(compare == 1)
print(compare == 21)
print(compare != 1)
print(compare != 21)
print(compare > -5)
print(compare > 5)
print(compare < 3)
print(compare < -3)
print(compare >= 1)
print(compare >= 0)
print(compare <= 2)
print(compare <= 1)

# 6. Створити змінні a=2, b=5, c=6. На основі цих змінних створити змінну d, значення якої має бути “256”
a = 2
b = 5
c = 6

d = str(a) + str(b) + str(c)
print(d)