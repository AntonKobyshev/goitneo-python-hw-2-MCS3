def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(contacts, name, phone):
    if name in contacts:
        return "❌ Contact already exists. Use 'change' to update the phone number."
    contacts[name] = phone
    return "✔️ Contact added."


def change_contact(contacts, name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return "✔️ Contact updated."
    else:
        return "❌ Contact not found."


def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "❌ Contact not found."


def show_all(contacts):
    if not contacts:
        return "❌ No contacts found."
    contact_list = "\n".join(
        [f"{name}: {phone}" for name, phone in contacts.items()])
    return contact_list


def main():
    contacts = {}
    print("🤖 Welcome to the assistant bot!")
    while True:
        user_input = input("⌨️ Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("🖐 Good bye!")
            break
        elif command == "hello":
            print("🖐 How can I help you?")
        elif command == "add":
            if len(args) == 2:
                name, phone = args
                print(add_contact(contacts, name, phone))
            else:
                print("❌ Invalid command.")
        elif command == "change":
            if len(args) == 2:
                name, new_phone = args
                print(change_contact(contacts, name, new_phone))
            else:
                print("❌ Invalid command.")
        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                result = show_phone(contacts, name)
                print(result)
            else:
                print("❌ Invalid command.")
        elif command == "all":
            result = show_all(contacts)
            print(result)
        else:
            print("❌ asdInvalid command.")


if __name__ == "__main__":
    main()
