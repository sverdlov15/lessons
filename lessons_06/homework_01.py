'''Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное,
в идеале не использовать библиотечные функции.'''

doc = "привет двадцать слон железо слон карта слон"
d = {}
for i in doc.split('\n'):
    for j in i.split():
        d[j] = d.get(j, 0) + 1

l = list(d.items())
l.sort(key=lambda x: x[1], reverse=True)
print(l)

d = sorted(doc.split( ))

print(max(d,key=len))
