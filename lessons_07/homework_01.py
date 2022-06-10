"""
Известно, что на шахматной доске 8×8 можно расставить коней так, чтобы они не били друг
друга (коней может ходить буквой "Г" (3 + 1)). Вам дана расстановка двух
коней на доске, определите могут ли кони бить друг друга.
Программа получает на вход две пары чисел, первое число в паре - координата по горизонтали,
второе - координата по вертикали. Если кони не бьют друг друга, выведите слово NO, иначе выведите YES.
"""


def check_coords(x1: int, y1: int, x2: int, y2: int) -> bool:
    return (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1)


if __name__ == "__main__":
    x1 = int(input("Enter X1:"))
    y1 = int(input("Enter Y1:"))

    x2 = int(input("Enter X2:"))
    y2 = int(input("Enter Y2:"))

    if check_coords(x1, y1, x2, y2):
        print("YES")
    else:
        print("NO")