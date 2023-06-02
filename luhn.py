import logging


def luhn_check(number_file: str):
    """
    Проверка корректности номера с помощью алгоритма Луна.
    :param number_file: Путь к файлу с номером карты.
    """
    try:
        with open(number_file, 'r') as f:
            number = f.read()
        logging.info("Данные из файла успешно считаны")
    except OSError as err:
        logging.warning(f"{err} Не удалось считать данные")
    logging.info(number)
    numbers = list(map(int, number))[::-1]
    logging.info(numbers)
    for i in range(1, len(numbers), 2):
        numbers[i] *= 2
        if numbers[i] > 9:
            numbers[i] = numbers[i] % 10 + numbers[i] // 10
    return sum(numbers) % 10 == 0