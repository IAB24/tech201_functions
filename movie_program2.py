def movie_program():
    age = int(input("How old are you?"))
    if int(age) > 0 and int(age) < 117:
        if int(age) >= 18:
            print("You are old enough to buy a ticket for any movie ")
        elif int(age) < 18 and int(age) >= 15:
            print("You can buy a ticket for films rated U, PG, 12 and 15")
        elif int(age) < 15 and int(age) >=12:
            print("You can buy tickets for films rated U, PG, and 12")
        else:
            print("You can buy tickets for any U rated films but adult is supervision still advised ")
    else:
        print("The value you've entered is invalid, please enter your age in digits")
movie_program()
