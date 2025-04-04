num = input("")
num1 = num.split()

第一字符 = int(num1[0])
第二字符 = int(num1[1])

商, 余数 = divmod(第一字符, 第二字符)

print(商, 余数)