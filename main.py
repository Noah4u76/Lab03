# Name: Noah Sanderson
# Date: 09/12/2024
# Purpose of file: importing contacts py

import contacts

def main():
    contact_list = []
    
    while True:
        print("*** Tuffy Titan Contact List ***")
        print("1. Print list")
        print("2. Add contact")
        print("3. Modify contact")
        print("4. Delete contact")
        print("5. Sort list by first name")
        print("6. Sort list by last name")
        print("7. Exit")
        
        try: choice = int (input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Choose menu number 1 to 7")
            continue
        
        if choice ==1:
            if not contact_list:
                print("The contact list is empty.")
            else:
                contacts.print_list(contact_list)
        
        elif choice == 2:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            contacts.add_contact(contact_list, first_name=first_name, last_name=last_name)
            print(f"Added contact: {first_name} {last_name}")

        elif choice ==3:
            try: 
                index = int(input("Enter index of contact to modify: "))
                first_name = input("Enter new first name: ")
                last_name = input("Enter new last name: ")
                if contacts.modify_contact(contact_list, first_name=first_name, last_name=last_name, index=index):
                    print(f"Modified contact at index {index}: {first_name} {last_name}")
                else:
                    print("Error: Index out of range.")
            except ValueError:
                print("Invalid input. Please enter a valid index.")
                
        elif choice == 4:
            try:
                index = int(input("Enter the index of the contact to delete: "))
                if contacts.delete_contact(contact_list, index=index):
                    print(f"Deleted contact at index {index}.")
                else:
                    print("Error: Index out of range.")
            except ValueError:
                print("Invalid input. Please enter a valid index.")
        
        elif choice == 5:
            contacts.sort_contacts(contact_list, column=0)
            print("Sorted contacts by first name.")
        
        elif choice == 6:
            contacts.sort_contacts(contact_list, column=1)
            print("Sorted contacts by last name.")
        
        elif choice == 7:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a number from 1 to 7.")

if __name__ == "__main__":
    main()
