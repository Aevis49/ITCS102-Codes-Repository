#Today we learn about list (November 17, 2026)
fruit1 = "apple"
fruit2 = "sampal"
fruit3 = "longgan"
fruit4 = "rambutan"
fruit5 = "itlog"
fruit_basket = ["apple", "sampalok", "longgan", "rambutan"]
print(fruit_basket)
print(fruit_basket[0])

#Append is used for adding an item in list (placed on the last)
fruit_basket.append("Peach")
fruit_basket.append("Anjo")
fruit_basket.append("Katmon")
fruit_basket.append("keso")
fruit_basket.append("yema")
print(fruit_basket)

#Concept: Index - the order of items(variables) in a list or dictionary
fruit_basket.insert(1, "Yelo")
print(fruit_basket)

#removal or deletion of list
fruit_basket.pop(1)
fruit_basket.remove('Anjo')
print(fruit_basket)

#list splicing
print(fruit_basket[-1])
print(fruit_basket[0:3])