'''Написать функцию, которая используя модуль requests скачивает файл сохраняет его на файловой системе,
функция имеет два параметра: ссылка на файл и имя на файловой системе. В качестве примера ссылки на файл можно
использовать лицензию из ГитХаба из вашего репозитория:
https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE'''

#импортируем модуль
import requests

#открываем файл записи


#делаем запрос
#send = requests.post("https://github.com/sverdlov15/lessons/blob/main/LICENSE.txt")

url = "https://github.com/sverdlov15/lessons/blob/main/LICENSE.txt")

r = request.get(url)

with open("https://github.com/sverdlov15/lessons/blob/main/LICENSE.txt, "wb")
as f:
    f.write(r.content)

записываем содержимое в файл



