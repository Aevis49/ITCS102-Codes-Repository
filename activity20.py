from getpass import getpass
u = "Aevis"
p = "Pokemon"

isLogged = False

while isLogged == False:
    user = input("Enter ur username: ")
    pword = getpass("Enter password: ")

    if pword == p and user == u:
        print("Login Successfully")
        isLogged = True

    else:
        print("Login Denied")
        isLogged = False
