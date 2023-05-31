import csv

# pliki csv - dane oddzielone są przecinkiem, srednik lub innym znakiem
# Radek,Zenek,Marek

fileds = ['name', 'branch', 'year', 'cgpa']
# ['radek','COE','2','9.1']

my_list_dict = [
    {'branch': 'COE', 'cgpa': '9.1', 'name': 'Radek', 'year': '2'},
    {'branch': 'COD', 'cgpa': '9', 'name': 'Sanchit', 'year': '3'},
]

filename = 'records.csv'

# newline='' - aby nie dodawał pustych lini pomiedzy wierszami
with open(filename, 'w', newline='') as csv_f:
    csvwriter = csv.DictWriter(csv_f, fieldnames=fileds)
    csvwriter.writeheader()
    csvwriter.writerows(my_list_dict)
