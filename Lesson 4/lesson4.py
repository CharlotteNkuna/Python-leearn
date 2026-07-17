#Basic If Else Statements

age = int(input("Enter your age: "))
section_pass = input("Do you have a VIP pass? (yes/no): ").lower()

if age >= 18 and section_pass.lower() == "yes":
    print("You have access to the VIP section!")
elif age >= 18: #else if for more possibilities
    print("You have access to the general section.")
else: 
    print("Access denied!!")