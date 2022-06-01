'''Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра.
В результате ее работы на печать выводятся значения переданных переменных, но только если они не равны None.
Получим, например, следующее сообщение: Переданы аргументы: var1 = 2, var3 = 10.'''

def three_args(*, var1, var2=None, var3=None):
    arguments = ', '.join([f'{arg[0]} = {str(arg[1])}' for arg in locals().items() if arg[1] is not None])
    print(f'Переданы аргументы: {arguments}')

three_args(var1=22)
three_args(var1='Python', var3=3)
three_args(var1='Python', var2=3, var3=9)


