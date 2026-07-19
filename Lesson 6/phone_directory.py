# Phone Directory Search

# Dictionary of contacts
contacts = {
    "Alice": "0821112222",
    "Bob": "0712345678",
    "Charlie": "0839876543"
}

# Ask the user for a name
name = input("Enter your friend's name: ")

# Check if the name exists
if name in contacts:
    print("Found! " + name + "'s number is " + contacts[name])
else:
    print("Contact not found.")