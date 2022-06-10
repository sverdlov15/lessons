"""Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5),
стоп (сброс скорости на 0), отображение скорости,
задний ход (изменение знака скорости)."""

class CAR:
    brand: str = None
    model: str = None
    release: int = None
    speed: int = 0

    def __init__(self, *args, **kwargs):
        self.brand = kwargs.get("brand")
        self.model = kwargs.get("model")
        self.release = kwargs.get("release")
        if kwargs.get("speed") is not None:
            self.speed = kwargs.get("speed")

    def talk(self):
        raise NotImplementedError

    def speedw(self):

        while speed < 100:
            speed += 5
            if speed == 100:
               continue


class bmw(CAR):
    def talk(self):
        print(f"{self.brand} is Black.")

if __name__ == "__main__":
    bmw_x6 = bmw(brand="BMW", model="x6", release=2020, speed=5)
    bmw_x6.talk()
    bmw_x6.speedw()

