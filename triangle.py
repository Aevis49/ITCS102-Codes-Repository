for x in range(5,0,-1):
    for y in range(x):
        print(" ", end= " ")
    for z in range(1, 7-x):
        print(z, end=" ")
    for o in range(5-x, 0, -1):
        print(o, end=" ")
    print()
