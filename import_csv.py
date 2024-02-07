import csv
path = 'results.csv'
with open(path, 'r') as routine:
    reader = csv.reader(routine)
    for row in reader:
        print(row)