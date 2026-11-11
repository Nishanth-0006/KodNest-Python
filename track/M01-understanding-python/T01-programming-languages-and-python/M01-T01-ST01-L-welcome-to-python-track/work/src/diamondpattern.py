# Solid Diamond Pattern

rows = int(input())

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")

    for j in range(2 * i + 1):
        print("*", end="")

    print()

for i in range(rows):
    for j in range(i + 1):
        print(" ", end="")

    for j in range(2 * (rows - i - 1) - 1):
        print("*", end="")

    print()
