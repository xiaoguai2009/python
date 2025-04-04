num = input("")
num1 = num.split()
count = len(num1)
if count == 1:
    num2 = input("")
    num4 = num1.append(num2)
    num5 = sum(map(int, num1))
    print(num5)
else:
    num3 = sum(map(int, num1))
    print(num3)
