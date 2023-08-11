
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY 
# и возвращает истину, если дата может существовать или ложь, если такая дата невозможна. 
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# И весь период действует григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

import sys

def date_or_not_date(day, month, year) -> bool:
        
        leap_check = _check_leap_year(year)

        if 0 < year < 10000:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if 0 < day < 32:
                    return True
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if 0 < day < 31:
                    return True
            elif month == 2:
                if 0 < day < 30 and leap_check:
                    return True
                elif 0 < day < 29:
                    return True
        return False



def _check_leap_year(year) -> bool:
    CHEKC_ONE = 4
    CHECK_TWO = 100
    CHECK_THREE = 400
    YEARS = range(1, 10000)

    if year in YEARS and year % CHEKC_ONE == 0 and year % CHECK_TWO != 0 or year % CHECK_THREE == 0:
        return True
    return False



def date_validator(year) -> str:

    if date_or_not_date(day, month, year):

        return 'Год високосный' if _check_leap_year(year) else 'Год не високосный'
    else:
        return f'Дата заполнена некорректно'


day, month, year = map(int, input("Введите дату в формате DD.MM.YYYY: ").split('.'))

print(date_or_not_date(day, month, year))
print(_check_leap_year(year))
print(date_validator(year))


# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

if __name__ == "__main__":
    day, month, year = sys.argv
    date_or_not_date(day, month, year)