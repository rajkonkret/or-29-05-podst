import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    csvreader = csv.reader(csv_f)

    # do fields zostanie przypisany pierwszy wiersz i wskaznik zostanie przsuniety na kolejny
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)
    print("Suma wierszy", csvreader.line_num)

print(fields)
print(rows)  # [['Radek', 'COE', '2', '9.1'], ['Sanchit', 'COD', '3', '9']]
print(rows[0])  # ['Radek', 'COE', '2', '9.1']
print(rows[0][0])  # Radek