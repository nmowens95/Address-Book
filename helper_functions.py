import json
import os


def add_contact():
    name = input("Name: ")
    number = input("Number: ")
    email = input("Email: ")
    sub_contact = [name, number, email]
    full_contact = {name: sub_contact}
    file = open("contacts.txt", "a+")
    file.write(json.dumps(full_contact))
    file.write("\n")
    file.close()



def delete_contact():
    with open("contacts.txt", "r") as input:
        with open("temt.txt", "w") as output:
            keyword = input("Name: ")
            for line in input:
                if keyword not in line.strip("\n"):
                    output.write(line)


def search_contact():
    with open("contacts.txt", "r") as f:
        search = input("Search: ")
        for _, line in enumerate(f):
            if search in line:
                print(line)
                break
            else:
                print("--No contact found--\n")


def exit_program():
    print("\n--Exiting contacts--\n")
    return exit()