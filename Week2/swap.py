# Function to swap two variables
def swap_variables(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    
    # Swapping using a temporary variable
    temp = a
    a = b
    b = temp
    
    print(f"After swapping: a = {a}, b = {b}")

# Main function to get user input
def main():
    # Taking input from the user
    a = input("Enter the first variable (a): ")
    b = input("Enter the second variable (b): ")
    
    # Calling the swap function
    swap_variables(a, b)

# Call the main function to execute
main()