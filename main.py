from helper_functions import *


def command_prompt():
    command = input("Pick: a/d/s/q: ")
    print()
    if command == "q":
        return exit_program()
    if command == "a":
        return add_contact()
    if command == "d":
        return delete_contact()
    if command == "s":
        return search_contact()
    raise Exception("Try a prompted command \n")
    

def main():
    while True:
        print("--Contact Book--")
        print("\n'a' - to add contact")
        print("'d' - to delete contact")
        print("'s' - to search contact")
        print("'q' - to exit contact book\n")
        print()

        command_prompt()
        
main()