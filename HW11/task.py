def stats():
    length = len(number_book)
    print(f"Phone book has {length} records")


def add():
    user_name = input("Write your first name and last name: ")
    if user_name in number_book:
        print("Phone book has already had your info")
    else:
        user_number = input("Write your phone number: ")
        number_book[user_name] = user_number


def delete_info():
    deleting = input("Write your first name and last name to delete your info: ")
    if deleting in number_book:
        del number_book[deleting]
        print("Deleting was successful")
    else:
        print("There's no such info in the phone book.")


def list_of_names():
    count = 1
    for key in number_book.keys():
        print(f"{count}. {key}")
        count += 1


def show_all_info():
    # ===== I decided to keep old version of fragment of code here in order to have opportunity
    # ===== to compare with try-except block
    #
    #
    # if user_name in number_book:
    #     user = number_book[user_name]
    #     print(f"{user_name} has number: {user}")
    # else:
    #     print("Unknown name.")
    user_name = input("Write your name: ")
    try:
        user = number_book[user_name]
    except KeyError:
        print("Unknown name.")
    else:
        print(f"{user_name} has number: {user}")


# Phone book has default key-values
number_book = {
    "Roosevelt Eric": "+380681326666",
    "Clinton Andriy": "+380683990000"
}

while True:
    print(
        "\nMenu\n"
        "1. Show quantity of records.\n"
        "2. Add record.\n"
        "3. Delete record.\n"
        "4. Show list of all names.\n"
        "5. Show all information about exact person\n"
        "6. Exit\n"
    )

    # ===== The same story here
    #
    # user_choice = input("Choose operation: ")
    # if user_choice.isdigit():
    #     user_choice = int(user_choice)
    # else:
    #     print("Input only numbers")
    #     continue

    user_choice = input("Choose operation: ")
    try:
        user_choice = int(user_choice)
    except ValueError:
        print("Input only numbers")

    else:
        match user_choice:
            case 1:
                stats()
            case 2:
                add()
            case 3:
                delete_info()
            case 4:
                list_of_names()
            case 5:
                show_all_info()
            case 6:
                break
            case _:
                print("Unknown command")
