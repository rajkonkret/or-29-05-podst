import requests as re

# pip install requests

url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'

response = re.get(url)
print(response)
# <Response [200]>
# 200 - ok
# 400 - bład, bad request, 404 - brak zasoby
# 300 - rózny
# 500 - błedy wewnetrne serwary

table = response.json()
print(table)
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
# 'rates': [{'no': '103/A/NBP/2023', 'effectiveDate': '2023-05-30', 'mid': 4.522}]} - słownik
print(table['rates'])  # [{'no': '103/A/NBP/2023', 'effectiveDate': '2023-05-30', 'mid': 4.522}] - lista
print(table['rates'][0])  # {'no': '103/A/NBP/2023', 'effectiveDate': '2023-05-30', 'mid': 4.522} - słownik
print(table['rates'][0]['mid'])  # 4.522
