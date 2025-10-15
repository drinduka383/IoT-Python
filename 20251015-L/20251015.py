import sys
import time

# while True:
#     username = str(input("Sheno username: "))
#     password = str(input("Sheno password: "))
#     if username == "drin":
#         if password == "kulleri":
#             print("Access granted!")
#             break
#         else:
#             print("Wrong password!\nPritni 5 sekonda per te provuar perseri.")
#             # time.sleep(5)
#     else:
#         print("Wrong username or password!\nPritni 5 sekonda per te provuar perseri.")
#         # time.sleep(5)

# print("You have a total of 3 attempts.\n")
# for i in range(3):
#     username = str(input("Enter username: "))
#     password = str(input("Enter password: "))
#     if username == "drin":
#         if password == "kulleri":
#             print("\nAccess granted!")
#             break
#         else:
#             print(f"\nWrong password!\nYou have {2-i} attempt(s) left.\n")
#     else:
#         print(f"\nWrong username or password!\nYou have {2-i} attempt(s) left.\n")

i = 3
while i > 0:
    username = str(input("Enter username: "))
    password = str(input("Enter password: "))
    if username == "drin":
        if password == "kulleri":
            print("\nAccess granted!")
            break
        else:
            print(f"\nWrong password!\nYou have {i-1} attempt(s) left.\n")
    else:
        print(f"\nWrong username or password!\nYou have {i-1} attempt(s) left.\n")
    i -= 1
    if i == 0:
        secondsLeft = 10
        while secondsLeft > 0:
            print(f"\rYou have to wait {secondsLeft} more second(s) to try again.", end="")
            secondsLeft -= 1
            time.sleep(1)
        i = 3
        print("\n")
"""

Taken from notepad.pw:

# 15.10.2025
import time
secret_username = "FIM"
secret_password = "1234"
tentimet = 3
sleep_timer = 10
initial_timer = 10

while tentimet > 0:
    username = input("Sheno username-in: ")
    password = input("Sheno password-in: ")

    if username == secret_username and password == secret_password:
        print("Lejohet çasja")
        break
    else:
        print("Gabim ne username ose password!")
        tentimet = tentimet - 1
        if tentimet != 0:
            print("Keni edhe " + str(tentimet) + " tentime")
        else:
            print("Mohohet hyrja.")
            sleep_timer = initial_timer
            while sleep_timer > 0:
                print("Ju lutem, prisni edhe " + str(sleep_timer) + " s")
                sleep_timer -= 1
                time.sleep(1)
            tentimet = 1
            initial_timer *= 2
"""
