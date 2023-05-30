from datetime import date, timedelta, datetime

today = date.today()
time = datetime.now()

print(today)  # 2023-05-30
print(type(today))  # <class 'datetime.date'>
print(time)  # 2023-05-30 14:56:37.511322
print(type(time))  # <class 'datetime.datetime'>

#  days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tommorow = today + timedelta(days=1)  # 2023-05-31
print(tommorow)

print(today.year)
print(today.month)

print(time.hour)

products = [
    {'sku': '1', 'exp_date': today, 'price': 100.0},
    {'sku': '2', 'exp_date': tommorow, 'price': 50},
    {'sku': '3', 'exp_date': today, 'price': 20.0},
    {'sku': '3', 'exp_date': today, 'price': 120.0},
    {'sku': '3', 'exp_date': tommorow, 'price': 220.0},
]

print(products)

for product in products:
    if product['exp_date'] != today:
        continue
    print(product)
    product['price'] *= 0.8  # p = p * 0.8

    print(f"""
    Price for sku= {product['sku']}
    is now {product['price']}""")
