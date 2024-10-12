# Define a function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Define a function to categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Main program
print("Body Mass Index (BMI) Calculator")
print("--------------------------------")

weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

bmi = calculate_bmi(weight, height)
category = categorize_bmi(bmi)

print(f"Your BMI is: {bmi:.2f}")
print(f"Your BMI category is: {category}")