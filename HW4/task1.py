some_text = input("Write here some text: ")


if some_text.isdigit():
    some_text = int(some_text)
    print("This is a number")
    if(some_text % 2 == 0):
        print("This is an even number")
    else:
        print("This is an odd number")
elif some_text.isalpha():
    print("This is a text")
    text_length = len(some_text)
    print(f"Length of this word: {text_length}")
else:
    print("idk what is this")