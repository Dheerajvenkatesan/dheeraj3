def calculate_salary():
    try:
        basic_salary = float(input("Enter the Basic Salary: "))

        if basic_salary < 0:
            print("Salary cannot be negative.")
            return
        hra = 0.20 * basic_salary
        da = 0.10 * basic_salary
        
        # Calculate Total (Gross) Salary
        total_salary = basic_salary + hra + da
        
        # Calculate Tax (5% of total salary)
        tax = 0.05 * total_salary
        
        # Calculate Net Salary (Total - Tax)
        net_salary = total_salary - tax
        print("-" * 30)
        print(f"Basic Salary:  ₹{basic_salary:,.2f}")
        print(f"HRA (20%):     ₹{hra:,.2f}")
        print(f"DA (10%):      ₹{da:,.2f}")
        print(f"Total Salary:  ₹{total_salary:,.2f}")
        print(f"Tax (5%):      ₹{tax:,.2f}")
        print("-" * 30)
        print(f"Net Salary:    ₹{net_salary:,.2f}")

    except ValueError:
        print("Invalid input. Please enter a numerical value for the salary.")
calculate_salary()