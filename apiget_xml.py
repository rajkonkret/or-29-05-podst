import requests
import xml.etree.ElementTree as ET

url = "http://api.nbp.pl/api/exchangerates/tables/A?format=xml"

response = requests.get(url)
print(response)

xml_data = response.content

print(xml_data)

root = ET.fromstring(xml_data)
table_name = root.find('.//Table').text
print(f"Tabela: {table_name}")  # Tabela: A

date = root.find('.//EffectiveDate').text
print(date)  # 2023-06-01
rates = root.findall('.//Rate')

print(rates)

for rate in rates:
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = rate.find('Mid').text
    print(f"{code}: {currency} - {mid}")
# 15:05
# THB: bat (Tajlandia) - 0.1217
# USD: dolar amerykański - 4.2399
# AUD: dolar australijski - 2.7578
# HKD: dolar Hongkongu - 0.5412
# CAD: dolar kanadyjski - 3.1231
# NZD: dolar nowozelandzki - 2.5465
# SGD: dolar singapurski - 3.1329
# EUR: euro - 4.5312
# HUF: forint (Węgry) - 0.01223
# CHF: frank szwajcarski - 4.6572
# GBP: funt szterling - 5.2707
# UAH: hrywna (Ukraina) - 0.1154
# JPY: jen (Japonia) - 0.03033
# CZK: korona czeska - 0.1912
# DKK: korona duńska - 0.6084
# ISK: korona islandzka - 0.030269
# NOK: korona norweska - 0.3794
# SEK: korona szwedzka - 0.3900
# RON: lej rumuński - 0.9123
# BGN: lew (Bułgaria) - 2.3167
# TRY: lira turecka - 0.2041
# ILS: nowy izraelski szekel - 1.1341
# CLP: peso chilijskie - 0.005243
# PHP: peso filipińskie - 0.0754
# MXN: peso meksykańskie - 0.2399
# ZAR: rand (Republika Południowej Afryki) - 0.2138
# BRL: real (Brazylia) - 0.8386
# MYR: ringgit (Malezja) - 0.9186
# IDR: rupia indonezyjska - 0.00028285
# INR: rupia indyjska - 0.051435
# KRW: won południowokoreański - 0.003207
# CNY: yuan renminbi (Chiny) - 0.5959
# XDR: SDR (MFW) - 5.6304