"""
Дан произвольный список, содержащий только числа.
Выведите результат сложения всех чисел больше 10.
"""

my_list = [7, 17, 33, 5, 6, 47, -10]

result = 0

for item in my_list:
    if item > 10:
        result += item

print(result)