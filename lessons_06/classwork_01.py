'''Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык.
Написать две функции, одна переводит слово с английского на русский,
где слово - это входной параметр, вторая функция - с русского на английский.
'''

d = {"apple":"яблоко",
     "green":"зелёный",
     "fly":"летать"

def eng_to_rus(word):
    return d[word]


def rus_to_eng(word):
    for key, value in d.items():
        if value == word:
            return key

print(end_to_rus("apple"))
print(end_to_rus("fly"))
print(end_to_rus("green"))