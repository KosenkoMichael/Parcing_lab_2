import csv
import time


def file_cut_date_and_data(path: str) -> None:
    """open file and cut it on 2 files (file with data and file with date)"""
    date = []
    data = []
    with open(path, "r", encoding="utf-8", newline="") as file:
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
    print("end")


def main() -> None:
    file_cut_date_and_data("dataset.csv")


if __name__ == '__main__':
    main()
