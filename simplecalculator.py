while True:
    num1=int(input("Enter first number:\n"))
    num2=int(input("Enter second number:\n"))
    print("perform Operation\n",
          "press 1 for Addition\n",
          "press 2 for subtraction\n",
          "press 3 for multiplication\n",
          "press 4 for Division\n"
          " press 5 for FloorDivision\n"
           )
    Operation =input("select your Operation\n")
    if Operation == '1':
        num=num1+num2
        print("Addition Operation ",num)
    elif Operation == '2':
        num=num1-num2
        print("Subtfraction Operation",num)
    elif Operation == '3':
        num=num1*num2
        print("Multiplication Operation",num)
    elif Operation == '4':
        num=num1/num2
        print("Division Operation",num)
    elif Operation == '5':
        num=num1//num2
        print("Floor Division Operation",num)
    else:
        print("Invalid Choice","Choose 1/2/3/4 for Operation")
    another_Operation = input("Press Y for continue - Press N for Exit\n")
    if another_Operation.lower() != 'y':
        print("Exit")
        break

