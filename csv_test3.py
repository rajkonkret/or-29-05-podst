import pandas as pd

# pip install pandas

data = pd.read_csv('records.csv')

print(data)
print(data.columns)

print(type(data))  # <class 'pandas.core.frame.DataFrame'>
print(data.values)
print(data.values[0])  # ['Radek' 'COE' 2 9.1]
print(data.items)