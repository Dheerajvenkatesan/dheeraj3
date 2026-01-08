def atm_withdrawal():
    balance = 5000 
    
    print(f"Current Balance: ₹{balance}")
    
    try:
        amount = int(input("Enter the amount to withdraw: "))
        if amount % 100 != 0:
            print("Error: Amount must be a multiple of 100 (e.g., 100, 200, 500).")
        elif amount > balance:
            print(f"Error: Insufficient balance. You only have ₹{balance}.")
        elif amount <= 0:
            print("Error: Please enter a valid positive amount.")
            
        else:
            balance -= amount
            print(f"Withdrawal Successful! Please collect your cash.")
            print(f"Updated Balance: ₹{balance}")
            
    except ValueError:
        print("Error: Please enter a numeric value.")
atm_withdrawal()