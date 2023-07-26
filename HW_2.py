# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

# num = int(input("Введите число: "))
# print(hex(num))
# sixt = ''
# hexx = '0123456789ABCDEF'
# SIX = 16

# while num > 0:
#     sixt = hexx[num % SIX] + sixt
#     num = num // SIX

# print(sixt)

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.


def process(num, div):
    # Преобразуем дроби из строк в числа
    numer1, denom1 = map(int, num.split("/"))
    numer2, denom2 = map(int, div.split("/"))

    # Вычисляем сумму дробей
    sum_num = numer1 * denom2 + numer2 * denom1
    sum_denom = denom1 * denom2
    sum_frac = (sum_num, sum_denom)

    # Вычисляем произведение дробей
    prod_num = numer1 * numer2
    prod_denom = denom1 * denom2
    prod_frac = (prod_num, prod_denom)

    return sum_frac, prod_frac

# Пример использования 
num = input("Введите первую дробь: ")
div = input("Введите вторую дробь: ")

sum_frac, prod_frac = process(num, div)

print(f"Сумма дробей {num} и {div} - {sum_frac[0]}/{sum_frac[1]}")
print(f"Произведение дробей {num} и {div} - {prod_frac[0]}/{prod_frac[1]}")
