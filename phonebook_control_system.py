from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be a 10-digit number")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        for p in self.phones:
            if p.value == phone_number:
                self.phones.remove(p)

    def edit_phone(self, current_number, new_number):
        for p in self.phones:
            if p.value == current_number:
                p.value = new_number

    def find_phone(self, number):
        for p in self.phones:
            if p.value == number:
                return p

    def __str__(self):
        phone_list = "; ".join(str(p) for p in self.phones)
        return f"Contact name: {self.name}, phones: {phone_list}"


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, contact):
        self.data[contact.name.value] = contact

    def find(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def delete(self, key):
        if key in self.data:
            del self.data[key]


# Приклад використання
if __name__ == "__main__":
    print("Test script:")

book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")
