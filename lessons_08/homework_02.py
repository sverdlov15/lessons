"""Создать программу, которая импортирует класс из предыдущей задачи,
создает объект и при инициализации устанавливает марку Mercedes, модель E500,
год выпуска 2000.
Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран."""

from homework_01 import CAR, bmw

class Mersedes(CAR):

    def talk(self):
        print(f"{self.brand} is meowing.")

class mers_01(Mersedes, bmw):
    pass


if __name__ == "__main__":
    MersedesCar = mers_01(brand="Mersedes", model="E200", release=2020, speed=100)
    MersedesCar.talk()
