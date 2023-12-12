def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return 'Name is not in contacts. Give me user name please'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Contact not found  Give me name and phone please'
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name]
    contacts[name] = phone
    return "Contact updated."

@input_error
def get_contact_phone(args, contacts):
    name = args[0]
    phone  = contacts[name]
    return phone

def show_all(contacts):
    if len(contacts) == 0:
        return "No contacts."
    res = ""
    for k,v in contacts.items():
        res = res + f"Contact {k} {v}."
    return res

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact_phone(args, contacts))
        elif command == "all":
            print(show_all( contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
