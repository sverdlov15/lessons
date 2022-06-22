'''Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id. '''

import sqlite3


def create_user(id: int, prod_name: str, price: int, quantity: int, comment: str):
    with sqlite3.connect("product.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO product (id, prod_name, price, quantity, comment)
            VALUES (?, ?, ?, ?, ?);
            """,
            (id, prod_name, price, quantity, comment),
        )
        session.commit()

if __name__ == "__main__":
    create_user(10250, "iphone 8", 800, 10, "black")
    create_user(10251, "iphone 10", 900, 12, "32gb")
    create_user(10252, "iphone 11", 1100, 8, "max")
    create_user(10253, "iphone 12", 1300, 6, "red")
    create_user(10254, "iphone 13", 1500, 20, "1tb")