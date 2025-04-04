num = input("")
num1 = num.split()
count = len(num1)
if count == 2:
    num2 = input("")
    if num2 == "":
        num6 = input("")
        num7 = num1.append(num6)
        num8 = sum(map(int, num1))
        print(num8)

else:
    num3 = sum(map(int, num1))
    print(num3)