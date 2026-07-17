#Username and messag formatter

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a bio about yourself: ")

username = f"{first_name[0]}.{last_name.lower()}"
print(f"Username: {username}")


print(f"Your full name is:{first_name.title()} {last_name.title()}")

#stripping removes whitespace from the beginning and end of the string
clean_bio = bio.strip()

#count display number of bio characters
bio_length = len(clean_bio)
print(f"Bio Length: {bio_length} characters")


#replace occurrences
updated_bio = clean_bio.replace("I am", "I'm")
print(f"Bio: {updated_bio}")
