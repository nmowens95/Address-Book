import json

def create_file():
    pass

def add_contact():
    name = input("Name: ")
    number = input("Number: ")
    email = input("Email: ")
    sub_direct = [name, number, email]
    new_contact = {name: sub_direct}
    file = open("contacts.txt", "a+")
    file.write(json.dumps(new_contact))
    file.write("\n")
    file.close()


def delete_contact():
    pass

def search_contact():
    pass

def exit_program():
    print("\n--Exiting contacts--\n")
    return exit()