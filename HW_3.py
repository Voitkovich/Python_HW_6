# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

def get_unique_num(numbers):
    uniq = []

    for number in numbers:
        if number in uniq:
            continue
        else:
            uniq.append(number)
    return uniq


numbers = [1, 2, 5, 3, 1, 77, 32, 77, 44, 1, 6]

print(get_unique_num(numbers))