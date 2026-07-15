
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int (input("Enter your age: "))
fav_number = float(input("Enter your favorite number: "))

print(f"Welcome, {name} {surname}!")

#Uppercase
print(f"Name in uppercase: {name.upper()}")
#Tittlecase
print(f"Name in tittlecase: {name.title()}")

age_in_months = age * 12
print(f"Your age in months is: {age_in_months}")

rounded_num = round(fav_number, 2)
print(f"Your favourite number rounded to 2 decimal place is: {rounded_num}")

#printing the data types of the variables
print(f"Data type of name: {type(name)}")
print(f"Data type of surname: {type(surname)}")
print(f"Data type of age: {type(age)}")
print(f"Data type of favourite number: {type(fav_number)}")
