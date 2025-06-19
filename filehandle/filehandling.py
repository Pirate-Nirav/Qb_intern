# Project: Contact Book with File Handling
# This project will allow users to add, view, update, delete, and save contacts using file handling.
 
# Features:
# Add Contact – Store name, phone, and email.
 
# View Contacts – Display all stored contacts.
 
# Update Contact – Modify existing details.
 
# Delete Contact – Remove a contact.
 
# Save Contacts – Store data in a file.
 
# Load Contacts – Retrieve saved data when the program starts.
 
# we will use the json module to process the program


# ### **Step 1: Write Functions**
# 1. `add_contact()` – Stores a contact under a label.
# 2. `view_contacts()` – Displays all stored contacts.
# 3. `delete_contact()` – Removes a contact based on label.
# 4. `save_contacts()` – Writes data to a JSON file.
# 5. `load_contacts()` – Reads data from the file.

import json
import re

class Contacts:
    contact_book = {}

    def __init__(self):
        Contacts.load_data()
        while True:
            print(f"""
            1. Add details 
            2. Get details 
            3. Search details
            4. Delete contact
            5. Exit
            """)
            try:
                user_input = int(input("Select one option: "))
                if user_input == 1:
                    count = int(input("How many details do you want to add? "))
                    for _ in range(count):
                        Contacts.add_details()
                elif user_input == 2:
                    Contacts.get_details()
                elif user_input == 3:
                    Contacts.search_details()
                elif user_input == 4:
                    Contacts.delete_contact()
                elif user_input == 5 :
                    break
                else:
                    print("Select a correct option...")
            except ValueError:
                print("Please enter a valid number.")
    @staticmethod
    def load_data():
        try:
            with open("details.json","r") as f:
                Contacts.contact_book = json.load(f)

        except FileNotFoundError:
            Contacts.contact_book = {}
    @staticmethod
    def add_details():
        label = input("Enter title: ")
        name = input("Enter the name: ")
        number = input("Enter the number: ")
        email = input("Enter the email: ")
        Contacts.contact_book = {
            label:{
            "name": name,
            "number": number,
            "email": email
        }
    }
        Contacts.save_details()

    @staticmethod
    def save_details():
        try:
            with open("details.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data.update(Contacts.contact_book)

        with open("details.json", "w") as file:
            json.dump(data, file, indent=4)    

    @staticmethod
    def get_details():
        try:
            with open("details.json") as file:
                data = json.load(file)
                print(json.dumps(data, indent=4))
        except FileNotFoundError:
            print("File does not exist")
        except json.JSONDecodeError:
            print("File content is invalid or empty")

    @staticmethod
    def search_details():
        try:
            with open("details.json") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("details.json not found.")
            return
        query = input("Enter name, number, or email to search: ").lower()
        found = False
        for label, details in data.items():
            name = details.get('name', '').lower()
            number = details.get('number', '')
            email = details.get('email', '').lower()
            if (query in name or query in number or query in email):
                print(f"Match Found in '{label}':\n  Name: {details['name']}, Phone: {details['number']}, Email: {details['email']}")
                found = True
        if not found:
            print("No matching contact found.")

    @staticmethod
    def delete_contact():
        try:
            with open("details.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No contacts found to delete.")
            return

        label_to_delete = input("Enter the title of the contact to delete: ")

        if label_to_delete in data:
            del data[label_to_delete]
            with open("details.json", "w") as file:
                json.dump(data, file, indent=4)
            print(f"Contact '{label_to_delete}' has been deleted.")
        else:
            print(f"No contact found with title '{label_to_delete}'.")
