'''1.Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.
   2.Создать таблицу покупок. Атрибуты: id, ссылка на пользователя, ссылка на продукт, количество.
Реализовать покупку продукта, вывод всех покупок пользователя, фильтрацию по произвольным параметрам.
   3.Создать программу с пользовательским интерфейсом позволяющим выбирать определенную функцию и вводить необходимые данные.
'''
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy_utils import create_database, database_exists

DB_PATH = Path(__file__).resolve().parent / "my_database.sqlite3"
DB_ECHO = True


def setup_db_engine() -> Engine:
    return create_engine(f"sqlite:////{DB_PATH}", echo=DB_ECHO)


def create_database_if_not_exists(engine: Engine):
    if not database_exists(engine.url):
        create_database(engine.url)


def get_products(database_name: str):
    with sqlite3.connect(database_name) as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT * FROM product;
            """
        )
        session.commit()
        return cursor.fetchall()


def create_product(database_name: str, name: str, price: float, quantity: int, comment: str):
    with sqlite3.connect(database_name) as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO product (name, price, quantity, comment)
            VALUES (?, ?, ?, ?);
            """,
            (name, price, quantity, comment)
        )
        session.commit()


def update_product(database_name: str, product_id: int, name: str, price: float, quantity: int, comment: str):
    with sqlite3.connect(database_name) as session:
        cursor = session.cursor()
        cursor.execute(
            """
            UPDATE product SET name = ?, price = ?, quantity = ?, comment = ? where id = ?;
            """,
            (name, price, quantity, comment, product_id)
        )
        session.commit()


def delete_product(database_name: str, product_id: int):
    with sqlite3.connect(database_name) as session:
        cursor = session.cursor()
        cursor.execute(
            """
            DELETE FROM product WHERE id = ?;
            """,
            (product_id,)
        )
        session.commit()