import csv
path = '/home/rafiwho/Py prac/routine.csv'
with open(path, 'r') as routine:
    csv_reader = csv.reader(routine)
    for row in csv_reader:
        print(row)