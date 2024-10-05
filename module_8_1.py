def add_everything_up(a, b):

    try:
        # условие проверки, что а и b - числа
        if (isinstance(a, (int, float))) == True and (isinstance(b, (int, float))) == True:

            res = round(a + b, 3)
        else:
            res = a + b
        # возврат работы функции когда ошибки нет
        return res

    except TypeError:
        # присвоение перменной res строковых значений суммы  a, b
        res = (str(a) + str(b))

        return res

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

