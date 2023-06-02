import hashlib
import multiprocessing as mp
from tqdm import tqdm
from typing import Optional, Union


def enumerate_number(hash: str, bin: str, last_numbers: str, core_number: int = mp.cpu_count()) -> Optional[str]:
    """
    Подбор номера карты c помощью хэша.
    :param hash: Хэш карты.
    :param bin: БИН номер карты.
    :param last_numbers: Последние 4 цифры карты.
    :param core_number: Количество ядер.
    """
    args = []
    for i in range(1000000):
        args.append((hash, f"{bin}{i:06d}{last_numbers}"))
    with mp.Pool(processes=core_number) as p:
        for result in p.starmap(check_number, tqdm(args, desc="Процесс нахождения номера карты: ", ncols=120)):
            if result:
                p.terminate()
                return result
    return None


def check_number(hash: str, card_number: str) -> Union[str, bool]:
    """
    Проверка соответствия номера с хэшем.
    :param hash: Хэш карты.
    :param card_number: Номер карты.
    """
    if hash == hashlib.sha3_384(card_number.encode()).hexdigest():
        return card_number
    return False
