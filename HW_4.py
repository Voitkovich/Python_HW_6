# Напишите функцию для транспонирования матрицы Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


matrix = [
    [3, 7, 34, 89, 55],
    [44, 9, 31, 30, 5],
    [53, 2, 7, 77, 33], 
]

rows = len(matrix)
columns = len(matrix[0])

new_matix = [[0]*rows for _ in range(columns)]
 
for i in range(rows):
    for j in range(columns):
        new_matix[j][i] = matrix[i][j]
 
for row in new_matix:
    print(row)


# Напишите функцию принимающую на вход только ключевые параметры(kwargs) 
# и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}

def revers_dict(**data):
   
    for key, value in data.items():
        print("{} = {}".format(value, key))

revers_dict(rev=True, acc="YES", stroka=4)
