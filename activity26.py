from activity25 import balik
from activity25 import box
from activity25 import sum
from activity25 import factorial



print("Choose what you want to do")
print("1 - Triangle")
print("2 - Sum")
print("3 - Box")
print("4 - Factorial")
print("5 - Exit")
choose = int(input("Enter: "))

while True:
    if choose == 1:
        
         for i in range(number, 0, -1):
                for x in range(1, i+1):
                    print("*", end=" ")
                print()
                balik(input("How big is the triangle"))
    elif choose == 2:
        pass
    elif choose == 3:
        pass
    elif choose == 4:
        pass
    elif choose == 5:
        pass
    else:
        print("Invalid Choice")
        break