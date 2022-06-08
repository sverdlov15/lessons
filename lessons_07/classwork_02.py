'''Написать функцию, которая будет вызывать задержку выполнения программы случайным
 образом от 1-й до 5-ти секунд. Написать декоратор, который
будет выводить на печать время выполнения этой функции (end_time - start_time).'''

import random
from time import sleep
from time import sleep

def my_decorator(func):
    def execution_time():
        start_time = datetime.now()
        func()
        end_time = datetime.now()
    return execution_time


def random_delay():
    sleep(random.randint(1,5))

random_delay()


if __name__ == "__main__":
    random_delay()


