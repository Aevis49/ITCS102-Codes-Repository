a = 9
b = 2
c = 2

print(a > b and c < 2)

#Changed the value of c
c = 4

print(a > b and c > 2)

print(a > b or c < 2 and c == b)	
print(a > b or c == b)
print(c == b and a>b or c<2)
print(not(c == b and a>b or c<2))

#order
# not, and, or
