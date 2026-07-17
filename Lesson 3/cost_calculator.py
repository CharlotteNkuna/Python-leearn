#MANIPULATING NUMBERS
kilometers = float(input("How many kilometres do you want to travel? "))
petrol_price = float(input("What is the current petrol price per litre? "))

liters_needed = kilometers / 10
total = liters_needed * petrol_price

print(f"Kilometers to drive: {kilometers} km")
print(f"Liters needed: {round(liters_needed, 2)} L")
print(f"Total fuel cost: R{round(total, 2)}")
