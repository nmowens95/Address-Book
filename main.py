from helper_functions import *


def prompt():
    command = input("Pick: a/d/s/q: ")
    if command == "q":
        return exit_program()
    elif command == "a":
        return add_contact()
    elif command == "d":
        #return delete_contact()
        print("\ndelete\n")
    elif command == "s":
        #return search_contact()
        print("\nsearch\n")
    else:
        print("Try a prompted command \n")
    

def main():
    while True:
        print("--Contact Book--")
        print("\n'a' - to add contact")
        print("'d' - to delete contact")
        print("'s' - to search contact")
        print("'q' - to exit contact book")
        print()
        prompt()
        
main()