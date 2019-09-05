print("Welcome to my database over people \nWhat would you like to do?")

while True:
    kek = True
    print("input 1 for searching")
    print("input 2 for adding new entery to the list")
    print("input 3 to exit")

    inn = str(input(""))


#~~~~~~~~~~~~~~~~~~~~~~~ exit ~~~~~~~~~~~~~~~~~~~~~~~
    if inn == "3":
        exit()

#~~~~~~~~~~~~~~~~~~~~ add entry ~~~~~~~~~~~~~~~~~~~~~
    elif inn == "2":
        print("Add your new entry. \n write back to go back to menu")
        while kek == True:

            fname = str(input("First name: ").lower())
            if fname == "exit":
                exit()
            elif fname == "back":
                kek = False
                continue
            lname = str(input("Last name: ").lower())
            if lname == "exit":
                exit()
            elif lname == "back":
                kek = False
                continue
            birth = str(input("Birthyear: ").lower())
            if birth == "exit":
                exit()
            elif birth == "back":
                kek = False
                continue
            gender = str(input("Gender: ").lower())
            if gender == "exit":
                exit()
            elif gender == "back":
                kek = False
                continue
            land = str(input("Land: ").lower())
            if land == "exit":
                exit()
            elif land == "back":
                kek = False
                continue
            email = str(input("Email: ").lower())
            if email == "exit":
                exit()
            elif email == "back":
                kek = False
                continue
            number = str(input("Number: ").lower())
            if number == "exit":
                exit()
            elif number == "back":
                kek = False
                continue

            addressbook = open("db.txt", "a")
            addressbook.write(fname + "|" + lname + "|" + birth + "|" + gender + "|" + land + "|" + email + "|" + number + "\n")
            addressbook.close()


#~~~~~~~~~~~~~~~~~~~~ Search entry ~~~~~~~~~~~~~~~~~~~~

    elif inn == "1":
        print("Search in the database! \n write back to go back to menu")
        while kek == True:

            name = input("please enter your name: ")
            name = name.lower()

            if name == "exit":
                exit()
            if name == "back":
                kek = False

            addressbook = open("db.txt")

            for line in addressbook:
                record = line.split('|')
                if record[0] == name:
                    found = True
                    break
                else:
                    found = False
                    continue

            if not found:
                print("Name not found in database")
            else:
                for i in record:
                    print(i, end = " ")
