import csv
import time


def N_cut_by_week(path: str) -> None:
    """open file and cut it on N files (1file = 1weak)"""
    day_x = ""
    for year in range(2008, 2024):
        for month in range(1, 12):
            for i in range(0, 5):
                with open(path, "r", encoding="utf-8", newline="") as file:
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
    print("end")


def main() -> None:
    N_cut_by_week("dataset.csv")


if __name__ == '__main__':
    main()
