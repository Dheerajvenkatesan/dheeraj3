def calculate_electricity_bill(units):
    total_bill = 0

    if units <= 100:
        total_bill = units * 2
    elif units <= 200:

        total_bill = (100 * 2) + ((units - 100) * 3)
    else:

        total_bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    return total_bill
try:
    consumed_units = float(input("Enter the number of units consumed: "))
    if consumed_units < 0:
        print("Units cannot be negative.")
    else:
        bill = calculate_electricity_bill(consumed_units)
        print(f"Total Electricity Bill: ₹{bill}")
except ValueError:
    print("Please enter a valid numerical value for units.")