a = int(input("enter a lucky number between 1 and 10 \n"))

match a:
    case 1:
        print("you won a charger")
    case 6:
        print("you won $3")
    case _:
        print("Better luck next time")