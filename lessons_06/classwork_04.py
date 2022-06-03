""""Использую функцию из предыдущей задачи, написать программу игру Блэкджек,
т.е. реализовать цикл в котором на каждом ходу у игрока спрашивается, достать ли следующую карту, в случае положительного ответа  - вытягивать случайную карту.
Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го."""

from classwork_03 import get_random_card

my_dict = {"J":2, "D":3}

def now_naminal():
    return my_dict[naminal]

n, _ = get_random_card()
value = naminal_to_value(n)

current_sum = value
 while True:
     choice = input(" asdfg [y/n]: ")
     if choice == "n":
         break

    n, _ = get_random_card()
    value = naminal_to_value(n)
    current_sum += value

    if current_sum > 21:
        print("lose")
        break

    if current_sum == 21:
        print("win")
        break

    if current_sum == 21:
        print("win")
        break


