import matplotlib.pyplot as plt
from enumeration import enumerate_number
import time


def visualize_stats(hash: str, bin: str, last_numbers: str, stats_file: str):
    """
    Создание гистограммы статистики для 4 ядер.
    :param hash: Хэш номера.
    :param bin:  БИН номер карты.
    :param last_numbers: Последние 4 цифры карты.
    :param stats_file: Путь к файлу с гистограммой.
    :return:
    """
    cores = []
    enumerate_time = []
    for i in range(4):
        t1 = time.perf_counter()
        enumerate_number(hash, bin, last_numbers, i+1)
        t2 = time.perf_counter()
        cores.append(i+1)
        enumerate_time.append(t2-t1)
    plt.figure(figsize=(18, 9))
    plt.xlabel('Processes')
    plt.ylabel('Time')
    plt.title('Statistics')
    plt.bar(cores, enumerate_time, color='red', width=0.5)
    plt.savefig(stats_file)