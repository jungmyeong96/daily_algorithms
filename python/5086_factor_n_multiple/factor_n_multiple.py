while 42 :
    num1, num2 = map(int, input().split())
    if num1 == 0 & num2 == 0:
        break
    elif num2 % num1 == 0:
        print("factor")
    elif num1 % num2 == 0:
        print("multiple")
    else:
        print("neither")

