#concatenation = adding or combining strings
talent = "" #empty string
t = (input("What are your talents? --> "))
talent += t + ", "
t1 = (input("More? --> "))
talent += t1 + ", "
t2 = (input("Lastly? --> "))
talent += t2 + ", " 
print("My talents are",talent,"and I am pretty good at them")