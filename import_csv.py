import csv
path = 'routine.csv'
with open(path, 'r') as routine:
    reader = csv.reader(routine)
    for row in reader:
        print(row)