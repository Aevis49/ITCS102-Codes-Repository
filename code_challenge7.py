size = int(input("how many stars in the do you need: "))

for x in range(1, size + 1):
    for y in range(size - x):
        print(" ", end="")
    for y in range(x):
        print("*", end=" ")
    print()

for x in range(size - 1, 0, -1):
    for y in range(size - x):
        print(" ", end="")
    for y in range(x):
        print("*", end=" ")
    print()
