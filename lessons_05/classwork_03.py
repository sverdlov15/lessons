"""Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - 
и возвращает название сезона, к которому относится этот месяц. Например, передаем 
2, на выходе получаем "Winter""""


def month_to_season(month)
    mapping = {
        "winter": [1, 2, 12],
        "spring": [3, 4, 5],
        "summer": [6, 7, 8],
        "autumn": [ 9, 10, 11],
    }
    for season, month_list in mapping.items():
        if mouth in mouth_list:
            return season


print(mouth_to_season())
