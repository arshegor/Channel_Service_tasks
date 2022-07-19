import requests
from decimal import Decimal

# Получение курса Рубль/Доллар c сайта ЦБ
def get_rate():
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    return data["Valute"]["USD"]["Value"]

# Конвертация валюты по курсу
def convert_valute(sum, rate):
    return float(Decimal(sum * rate).quantize(Decimal('0.01')))


