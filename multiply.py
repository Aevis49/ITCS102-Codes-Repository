mul = int(input("Multiply: "))

for x in range(1, mul):
    for y in range(1,mul):
        print(y, end = " ")
    print(x, "x", y, "=", x*y)