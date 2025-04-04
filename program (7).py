n = 0
while n == 0:
    temperatura = int(input(""))
    if 10 < temperatura <= 30:
        print("it's ok")
    elif 0 < temperatura <= 9:
        print("it's cold")
    elif temperatura < 0:
        print("it's cold\nwater would freeze")
    elif 30 < temperatura < 100:
        print("it's hot")
    elif temperatura >= 100:
        print("it's hot\nwater would boil")
    elif temperatura == 10:
        print("it's ok")
    elif 0 == temperatura:
        print("it's cold\nwater would freeze")