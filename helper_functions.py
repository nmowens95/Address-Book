import json

def add_contact():
    name = input("Name: ")
    number = input("Number: ")
    email = input("Email: ")
    print("--Contact added--")
    print()
    sub_contact = [name, number, email]
    full_contact = {name: sub_contact}
    file = open("contacts.txt", "a+")
    file.seek(1)
    file.write("\n")
    file.write(json.dumps(full_contact))
    

    file.close()


def delete_contact():
    with open("contacts.txt", "r+") as file:
        search = input("Search: ")
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if search not in line:
                file.write(line)
            else:
                file.truncate()
                print(f"--{search} Deleted--\n")
            

def search_contact():
    with open("contacts.txt", "r") as f:
        search = input("Search: ")
        for _, line in enumerate(f):
            if search in line:
                print(line)
                break
            else:
                print("--No Contact Found--\n")


def exit_program():
    print("\n--Exiting Contacts--\n")
    return exit()