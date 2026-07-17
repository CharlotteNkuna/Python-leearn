#Tracking individual letters
name = "Python"

print(name[0]) 
print(name[-1]) #shortcut to print last letter
print(name[2])


#Using string methods
town = "  Johannesburg  "

print(town.upper()) #uppercase
print(town.strip()) #removes whitespace from the beginning and end of the string


#Email system generator
first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()

username =f"{first[0]}{last}"
print(f"Your email is: {username.lower()}@university.co.za")