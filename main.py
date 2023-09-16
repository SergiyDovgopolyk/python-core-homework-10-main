from collections import UserDict



class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)  # Виклик конструктора батьківського класу


class Phone(Field):
    def __init__(self, number):
        if not self.validate_phone(number):
            raise ValueError("Invalid phone number format")
        super().__init__(number)

    @staticmethod
    def validate_phone(number):
        return len(number) == 10 and number.isdigit()


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        phone = Phone(number)
        self.phones.append(phone)

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)

    def edit_phone(self, old_number, new_number):
        if old_number in [phone.value for phone in self.phones]:
            self.remove_phone(old_number)
            self.add_phone(new_number)
        else:
            raise ValueError("Phone number not found")

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone

    def __str__(self):
        return f"Name: {self.name.value}, Phones: {[phone.value for phone in self.phones]}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join([str(record) for record in self.data.values()])
