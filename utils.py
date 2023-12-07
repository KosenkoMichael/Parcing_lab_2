import csv
import time
import os
from myiterator import Iterator
import datetime


def find_data_dataset(path: str, data: datetime) -> tuple | None:
    """ Function: find data in original dataset

    Args:
        path (str): path to original dataset
        data (str): date, we want to find

    Returns:
        tuple: ((date, we find), (data, we found))
    """
    try:
        with open(path, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if data == row[0]:
                    mass = []
                    for i in range(1, len(row)):
                        mass.append(row[i])
                    return (data, mass)
    except:
        return None


def find_data_datA_E(path_X: str, path_Y: str, data: datetime) -> tuple | None:
    """Find data in dataset (data, date)

    Args:
        path_X (str): path to .csv with date
        path_Y (str): path to .csv with data
        data (str): date, we want to find

    Returns:
        tuple: (date, data)
    """
    try:
        pos = 1
        with open(path_X, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if data == row[0]:
                    break
                pos += 1
        with open(path_Y, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                pos -= 1
                if pos == 0:
                    return (data, row)
    except:
        return None


def find_data_years(path: str, data: datetime) -> tuple | None:
    """Find date in dataset (years)

    Args:
        path (str): path to folder with datasets
        data (str): date, we want to find

    Returns:
        tuple: (date, data)
    """
    try:
        year = data[0:4]
        with open(f"{path}\\{year}-01-01-{year}-12-31.csv", "r", encoding="utf-8", newline="") as file_N:
            reader = csv.reader(file_N)
            for row in reader:
                if data == row[0]:
                    mass = []
                    for i in range(1, len(row)):
                        mass.append(row[i])
                    return (data, mass)
        time.sleep(0.01)
    except:
        return None


def find_data_weeks(path: str, data: datetime) -> tuple | None:
    """find date in dataset (weeks)

    Args:
        path (str): path to folder with datasets
        data (str): date, we want to find

    Returns:
        tuple: (date, data)
    """
    try:
        month = data[5:7]
        year = data[0:4]
        file_names = os.listdir(path)
        for file_name in file_names:
            file_path = os.path.join(path, file_name)
            if os.path.isfile(file_path) and month and year in file_name:
                with open(file_path, "r", encoding="utf-8", newline="") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if data == row[0]:
                            mass = []
                            for i in range(1, len(row)):
                                mass.append(row[i])
                            return (data, mass)
    except:
        return None


def next_iter(path: str) -> tuple:
    """get next date in file

    Args:
        path (str): path to dataset.csv 

    Returns:
        tuple: ((date, we find), (data, we found))

    Yields:
        Iterator[tuple]: ((date, we find), (data, we found))
    """
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            data = row[0]
            mass = []
            for i in range(1, len(row)):
                mass.append(row[i])
            yield (data, mass)


# 24.05.2022,+16,742,ЮЗ 3м/с,+13,743,ЮЗ 3м/с
data = "2022-05-24"
# print(find_data_dataset("dataset.csv", data))
# print(find_data_datA_E("1/X.csv", "1/Y.csv", data))
# print(find_data_years("2", data))
# print(find_data_weeks("3", data))

# iter = next_iter("dataset.csv")
# first = next(iter)
# print(first)
# second = next(iter)
# print(second)

iter = Iterator("dataset.csv")

for i in range(1,10):
    print(next(iter))
