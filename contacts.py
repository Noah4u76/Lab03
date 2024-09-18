# Name: Noah Sanderson
# Date: 09/12/2024
# Purpose of File: Write a Python program that performs as a Tuffy Titan Contact List which contains a list of contacts that can be modified or deleted.

# Format for contact page / header
def print_list(contacts):
    print("================= CONTACT LIST ==================")
    print(f'{"Index":<8}{"First Name":<22}{"Last Name":<22}')
    print(f'{"======":<8}{"====================":<22}{"====================":<22}')
    for i, contact in enumerate(contacts):
        print(f'{i:<8}{contact[0]:<22}{contact[1]:<22}')

# Add contact function (first and last name)
def add_contact(contacts,first_name="", last_name=""):
    
    contacts.append([first_name, last_name])

# Modify contacts
def modify_contact(contacts, first_name="", last_name="", index=0):

    if 0 <= index < len(contacts):
        contacts[index] = [first_name, last_name]
        return True
    return False

# Delete contacts
def delete_contact(contacts, index=0):
    
    if 0 <= index < len(contacts):
        del contacts[index]
        return True
    return False

# Sort contacts
def sort_contacts(contacts, column=0):
    if column == 0:
        contacts.sort(key=lambda x: x[0])
    elif column == 1:
        contacts.sort(key=lambda x: x[1])
    
    
    
    




