#Adding 2 numbers

num1 = input ("Enter the first number: ")
num2 = input("Enter the second number: ")

sum = int(num1) + int(num2)
print(sum)

#OR
print(int(num1) + int(num2))

#OR
first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))

total = first_num * second_num
print(total)



#Calculating the tip
bill = float(input("Enter the bill R "))
tip = 0.15 #Written in decimal form

value_tip = bill * tip

print(f"Here is the tip {value_tip}")
print(f"Total bill is {round(value_tip, 2)} rounded")

total = bill + value_tip

print(f"Here is the cost {total}")
print(f"Total cost is {round(total, 2)} rounded")
