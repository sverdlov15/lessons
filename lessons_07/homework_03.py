'''Дана база данных (в виде текстового файла) о продажах некоторого интернет-магазина.
Каждая строка входного файла представляет собой запись вида Покупатель,
Товар, Количество, Стоимость где Покупатель - имя покупателя (строка без пробелов), товар -
название товара (строка без пробелов), количество - количество приобретенных единиц товара.
   Создайте список и выведите на экран всех покупателей, а для каждого покупателя подсчитайте
общее количество приобретенных им товаров и их стоимость.
   Создайте список и выведите на экран все товары, а для каждого товара подсчитайте общее количество
приобретенных и их стоимость.
'''

from collections import defaultdict
from sys import stdin

clients = defaultdict(lambda: defaultdict(int))
for line in stdin.readlines():
    client, thing, value - line.split()
    clients[client][thing] += int(value)

for client in sorted(clients):
    print(client + ":")
    for thing in sorted(clients[client]):
        print(thing, clients[client][thing])





