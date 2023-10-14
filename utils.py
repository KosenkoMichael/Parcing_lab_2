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


file_cut_date_and_data()
