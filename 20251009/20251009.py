# Detyra 1

"""
username = input("Enter username: ")
password = input("Enter password: ")

if username == "drin":
    if password == "kulleri":
        print("Access granted!")
    else:
        print("Wrong password!")
else:
    print("Wrong username or password!")

"""

# Detyra 2


"""
mosha = int(input("Shenoni moshen tuaj: "))

if mosha >= 0:
    if mosha <= 4:
        print("Ti je personi me i vogel ndonjehere!")
    elif mosha <= 12:
        print("Ti je ende nje femije!")
    elif mosha <= 18:
        print("Ti je nje adoleshent!")
    elif mosha <= 30:
        print("Ti je nje i rritur i vogel!")
    elif mosha <= 65:
        print("Ti je pjese e klases punetore!")
    elif mosha <= 100:
        print("Ti je penzioner!")
    else:
        print("Ekzistenca juaj eshte e cuditshme!")
else:
    print("Ekzistenca juaj eshte e cuditshme! (ose ki bo gabim n'shtyp.)")

"""


# Detyra 3

"""
 while True:
    print("Drin")
"""

"""

i = 1
j = 1
while i <= 10 and j <= 4:
    print(i)
    i += 1
    if i == 10:
        i = 0
        j += 1
        print("\n")
"""
while True:
    name = input("Ju lutem shkruani emrin tuaj.\n")
    if name == "emrin tuaj":
        print("Faleminderit!")
        break
