# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')

import re

def def_to_str(stroka):
    *a,b,c = (re.split('[. /]+', stroka))
    
    for _ in a:
        lst_str = '/'.join(a)

    return lst_str, b, c

stroka_a = def_to_str('c:/Users/Vladislav/Desktop/deep_to_python/test.txt')
print(stroka_a)



 
# stroka = 'c:/Users/Vladislav/Desktop/deep_to_python/test.txt'
 
# *a,b,c = re.split('[. /]+', stroka, 6)        # разделен косой чертой и точкой
# print(a,b,c) 





# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии

# Ввод:
# name_list = ['Vlad', 'Den', 'Alex']
# salary_list = [1000, 2000, 3000]
# extra_list = ['10.25%', '15%', '20%']
# Вывод:
# {'Vlad': 102.5, 'Den': 300.0, 'Alex': 600.0}

def generator_dict(names, salarys,bonuses):
    return {name: salary * float(bonus[:-1])/100
            for name, salary, bonus  
            in zip(names, salarys, bonuses)}
       

name_list = ['Vlad', 'Den', 'Alex']
salary_list = [1000, 2000, 3000]
extra_list = ['10.25%', '15%', '20%']

print(generator_dict(name_list, salary_list, extra_list))



# Создайте функцию генератор чисел Фибоначчи


def fibonacci(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))