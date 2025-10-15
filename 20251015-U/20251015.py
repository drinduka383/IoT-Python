# i = 11
# while i > 0:
#     i -= 1
#     if i == 7:
#         continue
#     print(i)

# print("printi for:")
#
# for i in range(12, 16):
#     print(i)
#
#
# print("\n\nprinti while:")
#
# j = 1
# while j < 10:
#     print(j)
#     j += 2


# shkruani ni program qe printon vetem dhjeteshet

# print("printi for:")
# for i in range(0, 101, 10):
#     # if i % 10 == 0:
#     print(i)
#
#
# print("\n\nprinti while:")
#
# j = 0
# while j <= 100:
#     if j % 10 == 0:
#         print(j)
#     j += 1

# print("printi for cift:")
# for i in range(0, 101, 2):
#     print(i, end=", ")
#
# print("\n\nose...")
# for i in range(0, 101):
#     if i % 2 == 0:
#         print(i, end=", ")
#
#
# print("\n\n\nprinti for tek:")
# for i in range(0, 100, 2):
#     print(i+1, end=", ")
#
# print("\n\nose...")
# for i in range(0, 100):
#     if i % 2 == 0:
#         print(i+1, end=", ")

# for i in range(1, 51):
#     print(2*i - 1)
#
# n = int(input("Sa numra te printohen? : "))
# for j in range(1, n+1):
#     print(2*j - 1)

#
# for i in range(50, 20, -1):
#     print(i)
#
# print("\n\nose...")
#
# j = 50
# while j > 20:
#     print(j)
#     j -= 1

import random as r

for i in range(0, 5):
    print(r.randint(0, 100))
