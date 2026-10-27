size = int(input("how many stars: "))
for x in range(size):
    for y in range(x,size):
        print("*", end=" ")
    print()