import csv
import time


def file_cut_date_and_data():
    date = []
    data = []
    with open("dataset.csv", "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            date.append([row[0]])
            data.append([row[i] for i in range(1, 7)])
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
                if f".{year}" in row[0]:
                    data.append(row)
        time.sleep(0.1)
        with open(f"2\\{year}0101-{year}1231.csv", "w", encoding="utf-8", newline="") as file_N:
            writer = csv.writer(file_N)
            writer.writerows(data)
        time.sleep(0.1)
    print("end_2")
    # with open(f"{year}0101-{year+1}1231.csv", "w", encoding="utf-8", newline="") as file_N:
    # writer = csv.writer(file_N)
    # writer.writerows(row)


def N_cut_by_week():
    print('...')


file_cut_date_and_data()
N_cut_by_year()
N_cut_by_week()
