import time

print("hi")

for i in range(101):
    print(f"\rProgress: {i}%", end="")
    time.sleep(0.05)

print()  # To move to a new line after done

# so tldr, \r and end="" allow the string to be 'rewritten'
