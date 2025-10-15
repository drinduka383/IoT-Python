# Data types

# Explained int, unsigned int, among other datatypes.

# Basic login authentication

username = input("Enter username: ")
password = input("Enter password: ")

if username == "IoT":
    if password == "12345678":
        print("Access granted!")
    else:
        print("Wrong password!")
else:
    print("Wrong username or password!")
