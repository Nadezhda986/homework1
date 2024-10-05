first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# разница неравных длин строк из списков
first_result = (l1 - l2 for (s1, s2) in zip(first, second)
                if (l1 := len(s1)) != (l2 := len(s2)))
print(list(first_result))

# сравнение длин строк в одинаковых позициях
second_result = (len(first[i]) == len(second[i])
                 for i in range(min(len(first), len(second))))
print(list(second_result))