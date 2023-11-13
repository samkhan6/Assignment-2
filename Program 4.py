class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if not self.contacts:
            print("Address book is empty.")
        else:
            for contact in self.contacts:
                print("\nContact Details:")
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")


contact1 = Contact(name="John Doe", phone_number="123-456-7890", email="john.doe@example.com")
contact2 = Contact(name="Alice Smith", phone_number="987-654-3210", email="alice.smith@example.com")
contact3 = Contact(name="Bob Johnson", phone_number="555-123-4567", email="bob.johnson@example.com")

address_book = AddressBook()


address_book.add_contact(contact1)
address_book.add_contact(contact2)
address_book.add_contact(contact3)

address_book.display_contacts()
