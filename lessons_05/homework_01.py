'''Написать функцию, которая используя модуль requests скачивает файл сохраняет его на файловой системе,
функция имеет два параметра: ссылка на файл и имя на файловой системе. В качестве примера ссылки на файл можно
использовать лицензию из ГитХаба из вашего репозитория:
https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE'''

import requests


def download_file(link, name):
    r = requests.get(link)
    open(name, "wb").write(r.content)


download_file(
    "https://github.com/sverdlov15/lessons/blob/main/LICENSE.txt")



