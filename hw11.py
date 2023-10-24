from collections import UserDict
from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value
    
    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def __str__(self):
        return str(self.value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.date_value = datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Невірний формат дня народження. Використовуйте формат 'YYYY-MM-DD'.")
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        try:
            datetime.strptime(new_value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Невірний формат дня народження. Використовуйте формат 'YYYY-MM-DD'.")
        self._value = new_value


class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Номер телефону повинен складатися з 10 цифр.")
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not new_value.isdigit() or len(new_value) != 10:
            raise ValueError("Номер телефону повинен складатися з 10 цифр.")
        self._value = new_value

class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        if birthday:
            try:
                datetime.strptime(birthday, '%Y-%m-%d')
            except ValueError:
                raise ValueError("Невірний формат дня народження. Використовуйте формат 'YYYY-MM-DD'.")
            self.birthday = Birthday(birthday)
        else:
            self.birthday = None

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        old_phone_obj = self.find_phone(old_phone)
        if old_phone_obj is not None:
            old_phone_obj.value = new_phone
        else:
            raise ValueError("Телефон для редагування не існує.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
    
    def days_to_birthday(self):
        if self.birthday:
            today = datetime.today().date()
            next_birthday = datetime(today.year, self.birthday.date_value.month, self.birthday.date_value.day).date()
            if next_birthday < today:
                next_birthday = datetime(today.year + 1, self.birthday.date_value.month, self.birthday.date_value.day).date()
            return (next_birthday - today).days
        else:
            return None

    def __str__(self):
        phones_str = ', '.join(str(p) for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def iterator(self, N):
        for i in range(0, len(self.data), N):
            yield list(self.data.values())[i:i + N]


address_book = AddressBook()
record_with_birthday = Record("John Doe", "1990-05-20")
new_record = Record("Ann Heller", "2000-02-28")
address_book.add_record(record_with_birthday)
address_book.add_record(new_record)
new_record.add_phone("0852869490")


if __name__ == "__main__":
    for name, record in address_book.data.items():
        if record.birthday:
            days_to_birthday = record.days_to_birthday()
            phones = ', '.join(str(p) for p in record.phones)  
            if days_to_birthday is not None:
                print(f"Contact name: {name} | Days to birthday: {days_to_birthday} | Phones: {phones}")

