# contact_book.py

# Store all contacts here
contacts = []


# Function to add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully.")


# Function to search for a contact
def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


# Function to delete a contact
def delete_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully.\n")
            return

    print("Contact not found.")


# Function to view all contacts
def view_all():
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        print("----- Contact List -----")
        for contact in contacts:
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("------------------------")


# Main menu
while True:

    print("===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        name = input("Enter name to search: ")
        result = search_contact(name)

        if result:
            print("Contact Found")
            print("Name :", result["name"])
            print("Phone:", result["phone"])
            print("Email:", result["email"])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(name)

    elif choice == "4":
        view_all()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")