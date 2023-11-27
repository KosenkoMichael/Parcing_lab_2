import csv
import time
import os
from myiterator import Iterator


def find_data_dataset(path: str, data: str) -> tuple:
    """ Function: find data in original dataset

    Args:
        path (str): path to original dataset
        data (str): date, we want to find

    Returns:
        tuple: ((date, we find), (data, we found))
    """
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if data == row[0]:
                mass = []
                for i in range(1, len(row)):
                    mass.append(row[i])
                return (data, mass)
        return None


def find_data_datA_E(path_X: str, path_Y: str, data: str) -> tuple:
    """ Function: find data in dataset, wich was cut by DATA and DATE

    Args:
        path_X (str): path to file with DATEs
        path_Y (str): path to file with DATAs
        data (str): date, we want to find

    Returns:
        tuple: ((date, we find), (data, we found))
    """
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
        return None


def find_data_years(path: str, data: str) -> tuple:
    """Function: find data in dataset, wich was cut by years

    Args:
        path (str): path to folder with datasets
        data (str): date, we want to find

    Returns:
        tuple: ((date, we find), (data, we found))
    """
    year = data[6:10]
    with open(f"{path}\\{year}0101-{year}1231.csv", "r", encoding="utf-8", newline="") as file_N:
        reader = csv.reader(file_N)
        for row in reader:
            if data == row[0]:
                mass = []
                for i in range(1, len(row)):
                    mass.append(row[i])
                return (data, mass)
    time.sleep(0.01)
    return None


def find_data_weaks(path: str, data: str) -> tuple:
    """Function: find data in dataset, wich was cut by weaks

    Args:
        path (str): path to folder with datasets
        data (str): date, we want to find

    Returns:
        tuple: ((date, we find), (data, we found))
    """
    month = data[3:5]
    year = data[6:10]
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
data = "24.05.2022"
# print(find_data_dataset("dataset.csv", data))
# print(find_data_datA_E("1/X.csv", "1/Y.csv", data))
# print(find_data_years("2", data))
# print(find_data_weaks("3", data))

# iter = next_iter("dataset.csv")
# first = next(iter)
# print(first)
# second = next(iter)
# print(second)

# iter = Iterator("dataset.csv")

# for i in range(1,10):
#     print(next(iter))
