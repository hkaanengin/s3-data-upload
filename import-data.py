import csv

def read_file(file_name):
    with open(file_name) as csv_file:
        csv_file = csv.reader(csv_file, delimiter=',')
        print(csv_file)
        line_count=0
        for row in csv_file:
            print(row)

read_file(file_name='dollar-tl.csv')
