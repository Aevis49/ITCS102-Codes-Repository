money = 7449
a = money//1000 
rem = money %1000 #sheesh it actually worked, modulus is key?
b = rem//500
rem = money %500
c = rem//200
rem = money %200
d = rem//100
rem = money %100
e = rem//50
rem = money %50
f = rem//20
rem = money %20
g = rem//10
rem = money %10
h = rem//5
rem = money %5
i = rem//1

print("Money to deposit -->", money ,"pesos")
print("1000 - ", a)
print("500 - ", b)
print("200 - ", c)
print("100 - ", d)
print("50 - ", e)
print("20 - ", f)
print("10 - ", g)
print("5 - ", h)
print("1 - ", i)
print("Congratulations! You received a total of --> ", money ,"pesos")
