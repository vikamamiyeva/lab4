# TODO решите задачу
import json


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    total_sum = 0.0

    # Проходим по каждому словарю в списке
    for item in data:
        # Извлекаем значения "score" и "weight"
        score = item.get("score", 0)
        weight = item.get("weight", 0)

        # Вычисляем произведение и добавляем к общей сумме
        total_sum += score * weight

    # Возвращаем сумму, округленную до 3 знаков после запятой
    return round(total_sum, 3)


# Выводим результат
print(task())
