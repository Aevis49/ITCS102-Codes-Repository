#games
rpg = []
novel = []
gacha = []

while True:
    play = input("Do you play games? yes/no: ").lower()

    if play == 'yes':
        print("What type of game do you play? ")
        print("1 rpg \n2 novel \n3 gacha")

        p = int(input("Choose: "))

        if p == 1:
            print("So you like exploring around")
            add = input("Lets add the game to our collection: ")
            rpg.append(add)
        elif p == 2:
            print("So you like reading stories")
            add = input("Lets add the game to our collection: ")
            novel.append(add)
        elif p == 3:
            print("So you like collecting characters")
            add = input("Lets add the game to our collection: ")
            gacha.append(add)
        else:
            print("Invalid choice")
            continue

        con = input("Do you wanna proceed? yes/no: ").lower()
        if con == 'yes':
            continue
        else:
            break
    else:
        break
        
print("Here is the added list:")
print(rpg)
print(novel)
print(gacha)
