import logging
import json


def luhn_check(number_file: str) -> bool:
    """
    Проверка корректности номера с помощью алгоритма Луна.
    :param number_file: Путь к файлу с номером карты.
    """
    try:
        with open(number_file) as json_file:
            json_data = json.load(json_file)
        logging.info("Данные из файла успешно считаны")
    except OSError as err:
        logging.warning(f"{err} Не удалось считать данные")
    number = json_data["card_number"]
    numbers = list(map(int, number))[::-1]
    for i in range(1, len(numbers), 2):
        numbers[i] *= 2
        if numbers[i] > 9:
            numbers[i] = numbers[i] % 10 + numbers[i] // 10
    json_data["luhn_check"] = sum(numbers) % 10 == 0
    try:
        with open(number_file, 'w') as f:
            json.dump(json_data, f)
        logging.info(f'Результат проверки записан в {number_file}!')
    except OSError as err:
        logging.warning(f'{err} Ошибка при записи номера карты в {number_file}!')