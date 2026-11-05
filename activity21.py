sum = 0
tuloy = True
while tuloy == True:

    num = int(input("Please enter a number: "))

    if num == 0:
        print("The total of numbers are: ", sum)
        print("Process Terminated: No more to add(0)")
        break

    else:
        print("Number not found")
        sum+= num
        print("The sum of the numbers is: ", sum)
        continue