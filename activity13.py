#write a python program that accepts age as an integer
#after determine the age group label of the given age

age = int(input("what is your age? --> " ))

if age >= 1 and age <=5:
	print("Infant")
elif age >= 6 and age <= 12:
	print("Kid")
elif age >= 13 and age <=19:
	print("Teenager")
elif age >= 20 and age <= 29:
	print("Early adulthood")
elif age >= 30 and age <= 45:
	print("Adult")
elif age >= 46 and age <=59:
	print("Advanced adulthood")
elif age >= 60 and age <= 150:
	print("Senior")

else:
	print("INVALID")
	print("EITHER YOU DON'T EXIST YET OR YOU ARE A FOSSIL")