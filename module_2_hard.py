a = int(input("Введите число от 3 до 20: "))

if a < 3 or a >20:
    print("Введено ошибочное число!")
else:
    key = ""
    list = []

    for i in range (1, a-1):
        for j in range (i,a):
            if i != j:
                if a % (i + j) == 0 and a not in list:
                    key = key + str(i) + str(j)
                    list.append(str(i) + str(j))
    print("Ключ: ",key)

