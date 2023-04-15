import json


def stats():
    count = 0
    with open("number_book.json") as number_book:
        file_json_data = number_book.read()
        file_data = json.loads(file_json_data)
        for _ in file_data:
            count += 1
        print(f"Phone book has {count} records")


def add():
    founded_info = False
    with open("number_book.json") as number_book:
        file_json_data = number_book.read()
        file_data = list(json.loads(file_json_data))
        user_name = input("Write your first name and last name: ")
        for dictionary in file_data:
            dictionary = dict(dictionary)
            if user_name in dictionary.values():
                founded_info = True
                break
    if founded_info:
        print("Phone book has already had your info")
    else:
        user_number = input("Write your phone number: ")
        new_record = {"name": user_name, "phone": user_number}
        file_data.append(new_record)
        json_new_record = json.dumps(file_data)
        with open("number_book.json", "w") as number_book:
            number_book.write(json_new_record)


def delete_info():
    deleting_flag = False
    with open("number_book.json") as number_book:
        json_data = number_book.read()
        data = list(json.loads(json_data))

    deleting = input("Write your first name and last name to delete your info: ")
    for dictionary in data:
        dictionary = dict(dictionary)
        if deleting in dictionary.values():
            data.remove(dictionary)
            deleting_flag = True
            break

    if deleting_flag:
        with open("number_book.json", "w") as number_book:
            new_info = json.dumps(data)
            number_book.write(new_info)
            print("Deleting was successful")
    else:
        print("There's no such info in the phone book.")


def list_of_names():
    count = 1
    with open("number_book.json") as number_book:
        json_data = number_book.read()
        data = json.loads(json_data)
        for dictionary in data:
            dictionary = dict(dictionary)
            print(f"{count}. {dictionary.get('name')}")
            count += 1


def show_all_info():
    check = False
    with open("number_book.json") as number_book:
        json_data = number_book.read()
        data = json.loads(json_data)
        user_name = input("Write your name: ")
        for dictionary in data:
            dictionary = dict(dictionary)
            if user_name in dictionary.values():
                user_phone = dictionary.get("phone")
                check = True
                break
        if check:
            print(f"{user_name} has number: {user_phone}")
        else:
            print("Unknown name.")


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
