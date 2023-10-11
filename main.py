from helper_functions import *

def prompt():
    command = input("Pick: a/d/s/q: ")
    if command == "a":
        #return add_contact()
        print("add")
    elif command == "d":
        #return delete_contact()
        print("delete")
    elif command == "s":
        #return search_contact()
        print("search")
    if command == "q":
        #return exit_program()
        quit



def main():
    while True:
        print("'a' to add contact")
        print("'d' to delete contact")
        print("'s' to search contact")
        print("'q' to exit contact book")
        
        try:
            prompt()
        except:
            print("Invalid command")
            continue
        
main()