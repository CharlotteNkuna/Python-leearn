# Smart ATM Withdrawal Simulator

balance = 500

withdraw = float(input("How much money do you want to withdraw? R"))

if withdraw <= 0:
    print("Invalid amount. You must withdraw more than R0.")

elif withdraw <= balance:  # else if there are more possibilities
    balance = balance - withdraw
    print(f"Withdrawal successful! Remaining balance: R{balance}")

else:
    print("Declined. Insufficient funds.")