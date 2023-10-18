import csv
import time


class FileIterator:
    path = ""
    count = 0

    def __init__(self, path):
        self.path = path
        self.count = 0
        # print("i was created", self.path, " ", self.count)

    def next(self):
        with open(self.path, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            count = 0
            for row in reader:
                if self.count == count:
                    print(row)
                count += 1
        self.count += 1
        return self
