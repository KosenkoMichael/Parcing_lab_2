import csv
import time


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
    print("end")


def main():
    N_cut_by_year()


if __name__ == '__main__':
    main()
