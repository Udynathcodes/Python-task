import math

# Function to calculate the area of a circle
def calculate_area_of_circle(radius):
    area = math.pi * (radius ** 2)  # Area formula: π * r^2
    return area

# Main function to get user input and display the area
def main():
    # Taking input from the user
    radius = float(input("Enter the radius of the circle: "))
    
    # Calculating the area
    area = calculate_area_of_circle(radius)
    
    # Printing the result
    print(f"The area of the circle with radius {radius} is {area:.2f} square units.")

# Call the main function to execute
main()