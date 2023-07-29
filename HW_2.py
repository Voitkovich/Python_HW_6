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


# def process(num, div):
   
#     numer1, denom1 = map(int, num.split("/"))
#     numer2, denom2 = map(int, div.split("/"))

#     sum_num = numer1 * denom2 + numer2 * denom1
#     sum_denom = denom1 * denom2
#     sum_frac = (sum_num, sum_denom)

#     prod_num = numer1 * numer2
#     prod_denom = denom1 * denom2
#     prod_frac = (prod_num, prod_denom)

#     return sum_frac, prod_frac


# num = input("Введите первую дробь: ")
# div = input("Введите вторую дробь: ")

# sum_frac, prod_frac = process(num, div)

# print(f"Сумма дробей {num} и {div} - {sum_frac[0]}/{sum_frac[1]}")
# print(f"Произведение дробей {num} и {div} - {prod_frac[0]}/{prod_frac[1]}")


# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

def get_proc_min(number: float, procent: float) -> float:
   
    this_proc = number * procent / 100.0
    minus_proc = number - this_proc

    return minus_proc


def get_proc_plus(number: float, procent: float) -> float:
   
    this_proc = number * procent / 100.0
    plus_proc = number + this_proc

    return plus_proc


money = 0
rezult_money = 0
RITCH = 5000000
PROC_RITCH = 10
PROC_EVERY = 1.5
PROC_CASH_BACK = 3
COUNT = 0


while True:
            choice = float(input('Выберите пункт:\n'
                               '1. Пополнить счет\n'
                               '2. Снять деньги\n'
                               '3. Выход\n'
                               '4. Баланс\n'
                               '---------------------\n'
                               'Ваш выбор:'))
            COUNT += 1

            if COUNT % 3 == 0:
                  money = get_proc_plus(money, PROC_CASH_BACK)
                  print(f"Вам начислен кэшбэк 3% - \U0001F601 {money}")
            if choice == 3:
                break

            elif choice == 1:
                 plus_money = float(input("Введите сумму пополнения счета кратную 50: \n"))
                 if plus_money % 50 != 0:
                     print("Сумма должна быть кратна 50!\n")
                 if plus_money >= RITCH:
                       plus_money = get_proc_min(plus_money, PROC_RITCH)
                       print(f"Вычли с вас налог на роскошь 10% - остаток: {plus_money}")

                 money += plus_money

            elif choice == 2:
                 minus_money = float(input("Введите сумму снятия кратную 50: \n")) 

                 if minus_money % 50 != 0:
                       print("Сумма должна быть кратна 50!\n")
                       break

                 if money == 0 or minus_money > money:
                       print("На вашем счету недостаточно средств! \U0001F612 \n")  
                       break    
                 
                 rezult_money = money - minus_money
                 rezult_money = get_proc_min(rezult_money, PROC_EVERY)
                 print(f"Остаток на счете: {rezult_money}") 
                  

  
            elif choice == 4:
                 print(f"Остаток на вашем счету: {money - rezult_money}\n")


