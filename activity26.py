from activity25 import balik
from activity25 import box
from activity25 import sum
from activity25 import factorial
import os
os.system('cls')

while True:
    print("Choose what you want to do")
    print("1 - Triangle")
    print("2 - Sum")
    print("3 - Box")
    print("4 - Factorial")
    print("5 - Exit")
    choose = int(input("Pick which option: "))


    if choose == 1:
        os.system('cls')
        print("Triangle!!")
        big = int(input("What should be the size? "))
        balik(big)
        continue

    elif choose == 2:
        os.system('cls')
        print("You have choosen Summation!!")
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter second number: "))
        print(f"The sum of {num1} and {num2} is {sum(num1, num2)}")
        continue

    elif choose == 3:
        os.system('cls')
        print("You have choosen Box!!")
        n = int(input("How big should the box be? "))
        box(n)
        continue

    elif choose == 4:
        os.system('cls')   
        print("You have choosen Factorial!!")
        n = int(input("What to factorial? "))
        print(f"The factorial of {n} is {factorial(n)}")
        continue

    elif choose == 5:
        os.system('cls')
        print("You have choosen to Exit.")
        break
    else:
        os.system('cls')
        print("Invalid Choice")
        break
