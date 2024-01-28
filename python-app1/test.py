def greet(message):
    new_message = message.capitalize()
    print("hey hey")
    return new_message


user_entry = input("What greeting do yoi want? ")
greeting = greet(user_entry)
print(greeting)
