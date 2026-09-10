#Part A
sender_Name = input("What is your name --> ")
item = input("What is the Item? --> ")
isFragile = input("Fragile (True of False)? ")
weight = float(input("How heavy? (In kilograms) --> "))
distance = float(input("How far? (In kilometers) --> "))
is_express = input("Express? (True of False) --> ")
is_international = input("International? (True of False) --> ")

base_cost = weight*2.50 + distance*0.15

print("-----------------------------------------------------------")

#Part B
print("Sender name: ", sender_Name)
print("Item : ", item)

#Past Boolean = compared directly as string
#Boolean always resulted into True, even if the input was "False"
if isFragile == "True":
	print("Fragile : Yes")
elif isFragile == "False":
	print("Fragile : No")

print("Weight: ", weight, "Kg")
print("Distance: ", distance, "Km")

if is_express == "True":
	print("Express: Yes")
elif is_express == "False":
	print("Express: No")


if is_international == "True":
	print("International: Yes")
elif is_international == "False":
	print("International: No")





if distance <= 100 and weight <= 2 and is_express == "False" and is_international == "False":
	print("Free Shipping! Total = $",base_cost)

elif is_express == "True" and is_international == "True":
	print("Total = $",base_cost*1.40+50)

elif is_express == "True" or is_international == "True" and weight > 20:
	print("Total = $",base_cost*1.20+25)

elif weight > 30 or distance > 1000:
	print("Total = $",base_cost+30)

else:
	print("Invalid input")

   
