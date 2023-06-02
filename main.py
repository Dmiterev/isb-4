import os
import argparse
import logging
import json
from enumeration import enumerate_number
from stats import visualize_stats
from luhn import luhn_check

logger = logging.getLogger()
logger.setLevel('INFO')


def read_settings(file: str) -> dict:
    """
    Считывает настройки из файла.
    :param file: Путь к файлу.
    """
    try:
        with open(file) as json_file:
            json_data = json.load(json_file)
        logging.info('Настройки считаны!')
    except OSError as err:
        logging.warning(f'{err} ошибка при чтении файла {file}!')
    return json_data


def write_in_file(number_file: str, number: str) -> None:
    """
    Запись номера в файл.
    :param number_file: Путь к файлу.
    :param number: Номер карты.
    """
    try:
        with open(number_file, 'w') as f:
            f.write(number)
        logging.info(f'Номер карты записан в {number_file}!')
    except OSError as err:
        logging.warning(f'{err} Ошибка при записи номера карты в {number_file}!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-set', '--settings', type=str,
                        help='Использовать собственный файл c настройками. Указать путь к файлу')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-enu', '--enumeration', type=int,
                       help='Определение номера карты с помощью хэша. Указать количество процессов')
    group.add_argument('-sts', '--stats', help='Визуализация статистики')
    group.add_argument('-lun', '--luhn_algorithm', help='Проверка валидности номера карты с помощью алгоритма Луна')
    args = parser.parse_args()
    if args.settings:
        settings = read_settings(args.settings)
    else:
        settings = read_settings(os.path.join("data", "settings.json"))
    if settings:
        if args.enumeration:
            card_number = enumerate_number(settings["hash"], settings["bin"], settings["last_numbers"], args.enumeration)
            if card_number:
                logging.info(f"Полученный номер карты: {card_number}")
                write_in_file(settings["card_number"], card_number)
            else:
                logging.info("Номер карты не найден!")
        elif args.stats:
            visualize_stats(settings["hash"], settings["bin"], settings["last_numbers"], settings["stats"])
            logging.info('Гистограмма построена')
        elif args.luhn_algorithm:
            if luhn_check(settings["card_number"]):
                logging.info('Номер карты корректный!')
            else:
                logging.info('Номер карты не некорректный!')