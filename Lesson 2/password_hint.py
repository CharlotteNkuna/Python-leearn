#Manipulating strings

password = input("Enter your password: ")
password = password.strip()

#Grab the very first letter and the very last letter of the password using string indexing.
first_letter = password[0]
last_letter = password[-1]

print(f"Your password starts with: {first_letter} and ends with: {last_letter}")