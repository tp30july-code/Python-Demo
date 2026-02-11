num = int(input("enter a number"))
match num:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("tuesday")
    case 5:
        print("thusday")
    case 6:
        print("friday")
    case 7:
        print("saterday")
    case 4: 
        print("wednesday")
    case _:
        print("Enter number between 10 and 8")