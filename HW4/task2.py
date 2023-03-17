some_text = input("Write here some text: ")
if some_text.isdigit():
    some_text = int(some_text)

match some_text:
    case int():
        print("This is a number")
    case str():
        print("This is a text")
    case _:
        print("idk what is this")