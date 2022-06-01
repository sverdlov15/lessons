'''Ввести с клавиатуры строку, проверить является ли
строка палиндромом и вывести результат (yes/no) на экран.
Палиндром - это слово или фраза, которые одинаково читаются слева направо
и справа налево'''

palidrom = input()
l = len(palidrom)
l = l//2

for i in range(1):
    if palidrom[i] == palidrom[-1-i]:
        print("палидром")


user_string = input("Enter")
print("Yes" if user_string == user_string[::-1] else "No")

