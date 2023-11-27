import csv
import time


class Iterator:
    def __init__(self, path):
        with open(path, "r", encoding="utf-8", newline="") as file:
            text = file.readlines()
            self.limit = len(text)
        self.counter = 0
        self.path = path

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            with open(self.path, "r", encoding="utf-8", newline="") as file:
                reader = csv.reader(file)
                count = 0
                for row in reader:
                    if count == self.counter and row != "":
                        data = row[0]
                        mass = []
                        for i in range(1, len(row)):
                            mass.append(row[i])
                        return (data, mass)
                    count += 1
        else:
            return None
