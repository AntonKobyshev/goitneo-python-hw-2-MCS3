def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Give me name and phone please."
        except ValueError:
            return "Invalid input format. Please enter a valid name and phone number."
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "✔️ Contact added."


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    contacts[name] = new_phone
    return "✔️ Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]

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
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("🖐 Good bye!")
            break
        elif command == "hello":
            print("🖐 How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("❌ Invalid command.")


if __name__ == "__main__":
    main()
