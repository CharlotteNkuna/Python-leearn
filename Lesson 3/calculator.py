#MANIPULATING NUMBERS

first_num = float(input("Enter the first number:"))
second_num = float(input("Enter the second number:"))

total_addition = first_num + second_num
total_subtraction = first_num - second_num
total_multiplication = first_num * second_num


print(f"Total addition is {round(total_addition,2)}")
print(f"Total subtraction is {round(total_subtraction,2)}")
print(f"Total multiplication is {round(total_multiplication,2)}")

if second_num == 0:
    print("Error: Division by zero is not allowed.")
    print("Floor division cannot divide by 0.")
    print("Modulus division cannot divide by 0.")

else:
     total_division = first_num / second_num
     total_div = first_num // second_num
     total_mod = first_num % second_num

print(f"Total division is {round(total_division,2)}")
print(f"Total division is {round(total_div,2)}")
print(f"Total modulus is {round(total_mod,2)}")

