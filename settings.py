import logging
import json
import os

settings = {
    'hash': '78495810cec383f3f82049d03a522f5141583d1d6577235c74084c1d21f7a1df4612c05c0d6b5eb15edd1270ab5069f0',
    'bin': '220070',
    'last_numbers': '9920',
    'card_number': 'data/card_number.txt'
}


if __name__ == "__main__":
    try:
        with open(os.path.join('data', 'settings.json'), 'w') as f:
            json.dump(settings, f)
        logging.info("Настройки записаны в файл!")
    except OSError as err:
        logging.warning(f'{err} ошибка при записи в файл {"settings.json"}!')