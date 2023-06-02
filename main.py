import os
import argparse as args
import logging
import json

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


if __name__ == '__main__':
    parser = args.ArgumentParser()
    parser.add_argument('-set', '--settings', type=str,
                        help='Использовать собственный файл c настройками (Указать путь к файлу)')
    if args.settings:
        settings = read_settings(args.settings)
    else:
        settings = read_settings(os.path.join("data", "settings.json"))