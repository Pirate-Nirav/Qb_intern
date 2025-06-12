import re
class Contacts:
    contact_book = {}

    def __init__(self):
        while True:
            print(f"""
            1. Add details 
            2. Get details 
            3. Search details
            4. Exit
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
                    break
                else:
                    print("Select a correct option...")
            except ValueError:
                print("Please enter a valid number.")

    @staticmethod
    def add_details():
        label = input("Enter title: ")
        name = input("Enter the name: ")
        number = input("Enter the number: ")
        email = input("Enter the email: ")
        Contacts.contact_book[label] = {
            "name": name,
            "number": number,
            "email": email
        }

    @staticmethod
    def get_details():
        if not Contacts.contact_book:
            print("No contacts available.")
            return
        for label, details in Contacts.contact_book.items():
            print(f"{label}:\n  Name: {details['name']}, Phone: {details['number']}, Email: {details['email']}")

    @staticmethod
    def search_details():
        query = input("Enter name, number, or email to search: ").lower()
        found = False
        for label, details in Contacts.contact_book.items():
            if (query in details['name'].lower() or
                query in details['number'] or
                query in details['email'].lower()):
                print(f"Match Found in '{label}':\n  Name: {details['name']}, Phone: {details['number']}, Email: {details['email']}")
                found = True
        if not found:
            print("No matching contact found.")
