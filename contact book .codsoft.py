import json
class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.load_contacts()
    def load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                self.contacts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.contacts = []
    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)
    def add_contact(self, name, phone, email, address):
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        self.save_contacts()
    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']}")
    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
        return results
    def update_contact(self, name, new_details):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                contact.update(new_details)
                self.save_contacts()
                return True
        return False
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                return True
        return False
def main():
    book = ContactBook()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            book.add_contact(name, phone, email, address)
            print("Contact added successfully.")
        elif choice == "2":
            book.view_contacts()
        elif choice == "3":
            query = input("Enter name or phone to search: ")
            results = book.search_contact(query)
            if results:
                for contact in results:
                    print(contact)
            else:
                print("No matching contacts found.")
        elif choice == "4":
            name = input("Enter name of contact to update: ")
            new_phone = input("Enter new phone (leave blank to keep unchanged): ")
            new_email = input("Enter new email (leave blank to keep unchanged): ")
            new_address = input("Enter new address (leave blank to keep unchanged): ")
            new_details = {}
            if new_phone:
                new_details['phone'] = new_phone
            if new_email:
                new_details['email'] = new_email
            if new_address:
                new_details['address'] = new_address
            if book.update_contact(name, new_details):
                print("Contact updated successfully.")
            else:
                print("Contact not found.")
        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            if book.delete_contact(name):
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
