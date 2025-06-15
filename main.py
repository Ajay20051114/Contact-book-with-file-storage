# contact_book.py

FILE_NAME = "contacts.txt"

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("Contact added successfully!\n")

def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.\n")
                return
            print("\n--- Contact List ---")
            for contact in contacts:
                name, phone, email = contact.strip().split(",")
                print(f"Name: {name}, Phone: {phone}, Email: {email}")
            print()
    except FileNotFoundError:
        print("No contact file found. Start by adding a contact.\n")

def search_contact():
    search_name = input("Enter the name to search: ").lower()
    found = False
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                if search_name in name.lower():
                    print(f"Found - Name: {name}, Phone: {phone}, Email: {email}")
                    found = True
        if not found:
            print("No matching contact found.\n")
    except FileNotFoundError:
        print("Contact file not found.\n")

def delete_contact():
    name_to_delete = input("Enter the name to delete: ").lower()
    updated_contacts = []
    deleted = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                if name.lower() != name_to_delete:
                    updated_contacts.append(line)
                else:
                    deleted = True

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_contacts)

        if deleted:
            print("Contact deleted successfully!\n")
        else:
            print("Contact not found.\n")
    except FileNotFoundError:
        print("No contact file exists.\n")

def main():
    while True:
        print("------ Contact Book ------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.\n")

if __name__ == "__main__":
    main()
