Action = str(input("What action you want to perform \n"))
Action = Action.lower()
match Action:
    case "sum":
        number1 = int(input("Enter the number 1 that you want to add \n"))
        number2 = int(input("Enter the number 2 that you want to add \n"))
        result = number1 + number2
        print("Your answer is",result)

    case "subtract":
        number1 = int(input("Enter the number 1 you want to subtract \n"))
        number2 = int(input("Enter the number 2 you want to subtract \n"))
        result = number1 - number2
        print("Your answer is",result)

    case "divide":
        number1 = int(input("Enter the number 1 you want to divide \n"))
        number2 = int(input("Enter the number 2 you want to divide \n"))
        result = number1 / number2
        print("Your answer is",result)

    case _:
        print("Error")