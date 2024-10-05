first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer',
                  'Assembler']

# длины строк (не менее 5 символов)
first_result = [l for s in first_strings if (l := len(s)) >= 5]
print(first_result)

# пары слов одинаковой длины из двух списков
second_result = [(s1, s2) for s1 in first_strings
                          for s2 in second_strings
                          if len(s1) == len(s2)]
print(second_result)

# словарь {строка: длина строки} из объединённых списков
third_result = {s: l for s in first_strings + second_strings
                if not (l := len(s)) % 2}
print(third_result)