# Initialize variables to store income and expenses
income = 0
expenses = {}

# Function to add an expense
def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    expenses[description] = amount

# Function to calculate total expenses
def calculate_total_expenses():
    total = 0
    for amount in expenses.values():
        total += amount
    return total

# Function to calculate net savings
def calculate_net_savings():
    total_expenses = calculate_total_expenses()
    net_savings = income - total_expenses
    return net_savings

# Main program
print("Net Savings Calculator")
print("---------------------")

# Get income
income = float(input("Enter your monthly income: "))

# Add expenses
while True:
    print("1. Add an expense")
    print("2. Calculate net savings")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        net_savings = calculate_net_savings()
        print(f"Your net savings is: ${net_savings:.2f}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")