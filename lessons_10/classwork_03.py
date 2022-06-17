"""Создать функцию при помощи регулярных выражений для проверки, что строка является валидным телефонным номером
в формате
+375 (29) 299-29-29."""

import re

def is_phone(string):
    return re.search(r"^\+\d{3} \(\d{2}\) \d{3}-\d{2}-$", string)

if __name__ == "__main__":
    for item in("+375 (29) 299-29-29,+375 (29) 299-29-29"):
        assert is_phone(item) is not None

    for item in("+375 (29) 299-29-29,+375 (29) 299-29-29"):
        assert is_phone(item) is None




