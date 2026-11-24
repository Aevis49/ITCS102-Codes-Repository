def balik(number):
    for i in range(number, 0, -1):
        for x in range(1, i+1):
            print("*", end=" ")
        print()

def sum(a, b):
    return(a+b)

def box(size):
    for x in range(size+1):
        for y in range(size+1):
            if x == 0 or x == size or y == 0 or y == size:
                print("*", end=" ")
            else: 
                print(" ", end= " ")
        print()

def factorial(number):
    fact = 1
    for x in range(number, 0, -1):
        fact *= x
    return fact


balik(5)
balik(10)
balik(9)

print(sum(1,2))
print(sum(60,7))
print(sum(67,91)*100)

box(10)

print(factorial(4))