contacts = {}  # Dictionary to store contacts (name: phone number)

def add_contact():
  """Adds a new contact to the dictionary."""
  name = input("Enter name: ")
  phone_number = input("Enter phone number: ")
  contacts[name] = phone_number
  print("Contact added successfully!")

def view_contacts():
  """Prints all contacts."""
  if not contacts:
    print("There are no contacts in the book.")
  else:
    print("Contacts:")
    for name, phone_number in contacts.items():
      print(f"{name}: {phone_number}")

def search_contact():
  """Searches for a contact by name."""
  name = input("Enter name to search: ")
  if name in contacts:
    print(f"Contact: {name}, Phone Number: {contacts[name]}")
  else:
    print("Contact not found.")

def main():
  """Main loop for user interaction."""
  while True:
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      add_contact()
    elif choice == "2":
      view_contacts()
    elif choice == "3":
      search_contact()
    elif choice == "4":
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()