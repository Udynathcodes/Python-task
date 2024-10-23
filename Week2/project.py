# List of contacts, each represented as a dictionary
contacts = [
    {"name": "Alice Johnson", "phone": "123-456-7890", "email": "alice@example.com"},
    {"name": "Bob Smith", "phone": "987-654-3210", "email": "bob@example.com"},
    {"name": "Charlie Brown", "phone": "555-555-5555", "email": "charlie@example.com"}
]

# Function to print all contacts
def print_contacts():
    print("Contacts List:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Function to update a contact's information
def update_contact(name, phone=None, email=None):
    for contact in contacts:
        if contact['name'] == name:
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            print(f"Updated contact: {contact}")
            return
    print("Contact not found.")

# Function to add a new contact
def add_contact(name, phone, email):
    new_contact = {"name": name, "phone": phone, "email": email}
    contacts.append(new_contact)
    print(f"Added new contact: {new_contact}")

# Function to remove a contact
def remove_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'] != name]
    print(f"Removed contact: {name}")

# Main function to demonstrate the functionality
def main():
    # Print initial contacts
    print_contacts()
    
    # Update a contact
    update_contact("Alice Johnson", phone="111-222-3333")
    
    # Add a new contact
    add_contact("David Wilson", "444-444-4444", "david@example.com")
    
    # Remove a contact
    remove_contact("Bob Smith")
    
    # Print contacts after modifications
    print_contacts()

# Call the main function to execute
main()