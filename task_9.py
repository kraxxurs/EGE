import csv

with open ("9-257.csv") as file:
    reader = list(csv.reader(file, delimiter = ","))

for row in reader:
    row = list(map(int, row))
    if row == sorted(row, reverse = True) and len(set(row)) == 7:
        avg_1 = (max(row) + min(row)) / 2
        avg_2 = (sum(row) - max(row) - min(row)) / 5
        if avg_1 > avg_2:
            print(sum(row))
