import csv
import time


def file_cut_date_and_data():
    date = []
    data = []
    with open("dataset.csv", "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            date.append([row[i] for i in range(0, 3)])
            data.append([row[i] for i in range(3, 9)])
    with open("1\\X.csv", "w", encoding="utf-8", newline="") as file_x:
        writer = csv.writer(file_x)
        writer.writerows(date)
    with open("1\\Y.csv", "w", encoding="utf-8", newline="") as file_y:
        writer = csv.writer(file_y)
        writer.writerows(data)
    print("end_1")


def N_cut_by_year():
    for year in range(2008, 2024):
        data = []
        with open("dataset.csv", "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] == f"{year}":
                    data.append(row)
        time.sleep(0.1)
        with open(f"2\\{year}0101-{year}1231.csv", "w", encoding="utf-8", newline="") as file_N:
            writer = csv.writer(file_N)
            writer.writerows(data)
        time.sleep(0.1)
    print("end_2")


def N_cut_by_week():
    day_x = ""
    for year in range(2008, 2024):
        for month in range(1, 12):
            for i in range(0, 5):
                with open("dataset.csv", "r", encoding="utf-8", newline="") as file:
                    reader = csv.reader(file)
                    data = []
                    for row in reader:
                        for day in range(1+7*i, 8+7*i):
                            if row[0] == f"{day}" and row[1] == f"{month}" and row[2] == f"{year}":
                                data.append(row)
                                day_x = row[0]
                time.sleep(0.1)
                if len(data):
                    with open(f"3\\{year}.{month}.{1+7*i}-{year}.{month}.{day_x}.csv", "w", encoding="utf-8", newline="") as file_N:
                        writer = csv.writer(file_N)
                        writer.writerows(data)
                time.sleep(0.1)
    print("end_3")


file_cut_date_and_data()
N_cut_by_year()
N_cut_by_week()
