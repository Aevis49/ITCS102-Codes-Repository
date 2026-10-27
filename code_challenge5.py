
size = int(input("Input the number of x: "))
for x in range(size):
    for y in range(size):
        if y+x ==size -1 or x==y:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

            