num = int(input("Enter any number "))
match num : 
    case 0:
        print("number is zero")
    case 4:
        print("number is four")
    case _:
        print("the number is invalid")