# Function to get user input and print the formatted message
def user_info():
    # Taking input from the user
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    weight = input("Enter your weight (in kg): ")

    # Printing the formatted output
    print(f"My name is {name}, and I am {age} years old. I weigh {weight} kg.")

# Call the function to execute
user_info()