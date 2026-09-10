sender_Name = input("What is your name --> ")
item = input("What is the Item? --> ")
isFragile = bool(input("Fragile (True of False)? "))
weight = float(input("How heavy(In KG)> --> "))
distance = float(input("How far? --> "))
is_express = bool(input("Express? (True of False) --> "))
is_international = bool(input("International? (True of False) --> "))


base_cost = weight*2.50 + distance*0.15

#empty space to organize how?????

print("Sender name: ", sender_Name)
print("Item : ", item)


if isFragile == True:
	print("Fragile : Yes")

print("Weight: ", weight)
print("Distance: ", distance)
if is_express == True:
	print("Express: Yes")
if is_international == True:
	print("International: Yes")




if weight >= 100 and weight <= 2:
	print("Free Shipping! Total = $",base_cost)

elif is_express == True and is_international == True:
	print("Total = $",base_cost*1.40+50)

elif is_express == True or is_international == True and weight >= 20:
	print("Total = $",base_cost*1.20+25)

elif weight > 30 or distance > 1000:
	print("Total = $",base_cost+30)

else:
	print("Invalid input")

   
