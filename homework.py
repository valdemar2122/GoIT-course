contacts = {}

def user_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Invalid input. Please try again."
        except KeyError:
            return "Contact not found. Please try again."
        except ValueError:
            return "Invalid input format. Please try again."
        except TypeError as e:
            if "missing 1 required positional argument" in str(e):
                return "Please provide a name after 'phone'."
            else:
                raise e
    return inner

@user_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Added contact {name=}, {phone=}"

@user_error
def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return f"Changed contact {name=}, {new_phone=}"
    else:
        return f"Contact {name} not found. Please try again."

@user_error
def show_contact(name):
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        return f"Contact {name} not found. Please try again."


def show_all_contacts():
    return contacts

def unknown(*args):
    return "Unknown command, try again"

def parser(text: str):
    for func, kw in COMMANDS.items():
        if text.startswith(kw):
            return func, text[len(kw):].strip().split()
    return unknown, []

COMMANDS = {
    add_contact: 'add contact',
    change_contact: 'change contact',
    show_contact: 'phone ',
    show_all_contacts: 'show all'
}

def main():
    while True:
        user_input = input('>>>').lower()
        if user_input == 'exit':
            print("Good bye!")
            break
        func, data = parser(user_input)
        if func is not None and data is not None:
            print(func(*data))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
