'''Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран. Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.
Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут имени у объекта. Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.
Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод bark на meow.
Создать общий класс Animal, содержащий все общие методы классов Dog и Cat. Унаследовать Dog и Cat от класса Animal и Удалить в дочерних классах те методы, которые имеются у родительского класса. Создать объект каждого класса и вызвать все его методы.
'''



from classwork_01 import Dog


class NewDog(Dog):

    def change_name(self, new_name):
        self.name = new_name


if __name__ == "__main__":
    dog1 = NewDog(height=10, weight=5, name="First name")
    print("Old name: ", dog1.name)
    dog1.change_name("New name")
    print("New name: ", dog1.name)
