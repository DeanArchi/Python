user_input = input("Enter some text: ")

for letter in user_input:
    if letter.isdigit():
        letter = int(letter)
        print(f"This is a number {letter}")
        if letter % 2 == 0:
            print("This is an even number \n")
        else:
            print("This is an odd number \n")
    elif letter.isalpha():
        print(f"This is a letter '{letter}'")
        if letter.isupper():
            print("This is an upper letter \n")
        elif letter.islower():
            print("This is a lower letter \n")
    else:
        print(f"This is a symbol '{letter}' \n")