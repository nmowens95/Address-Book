import json


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
    name = input("Name: ")
    with open("contacts.txt", "r") as r:
        lines = r.readlines()
    with open("contacts.txt", "w") as w:
        for line in lines:
            if line.strip("\n") != current_contacts:
                w.write(line)
# Need to add logic to check key value and delete dictionary if True

def search_contact(current_contacts):
    with open("contacts.txt", "r"):
        for current in current_contacts:
            try:
                if current == current_contacts:
                    return current
            except Exception as err:
                print(err)
                break
                
                    
def exit_program():
    print("\n--Exiting contacts--\n")
    return exit()