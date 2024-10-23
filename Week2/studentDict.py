# Define the dictionary with student data
students_data = {
    "student1": {"name": "John Doe", "Reg_NO": "S101", "gender": "Male"},
    "student2": {"name": "Jane Smith", "Reg_NO": "S102", "gender": "Female"},
    "student3": {"name": "Bob Johnson", "Reg_NO": "S103", "gender": "Male"},
    "student4": {"name": "Alice Brown", "Reg_NO": "S104", "gender": "Female"},
    "student5": {"name": "Mike Davis", "Reg_NO": "S105", "gender": "Male"}
}

# Function to print student data in the required format
def print_student_data(student_data):
    for student, data in student_data.items():
        print(f"{data['name']} with Reg NO {data['Reg_NO']} is a {data['gender']}")

# Print the student data
print_student_data(students_data)