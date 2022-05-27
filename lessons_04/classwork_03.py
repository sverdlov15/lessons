'''Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n
(включая n) используя цикл while.'''

n = int(input("write:"))
result = 0
index = 0

for item in range(1, n+1):
    result += item**3
    pass

while index <= n:
    index += 1
    result += index**3

while n> 0:
    result += n**3
    n-=1

for item in range (1, n+1):
    result += item**3
