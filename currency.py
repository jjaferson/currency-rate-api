from enum import Enum
import json
from json import JSONEncoder
import time



class CurrencyType(Enum): 
    EURO = "EUR"
    REAL = "BRL"

class Currency():
    name = None
    value = None

    def __init__(self, name, value):
        self.name = name
        self.value = value

class CurrencyRate(): 
    date = None
    base = None
    rates = []

    def __init__(self, baseCurrency):
        self.date = int(round(time.time() * 1000))
        self.base = baseCurrency
        self.rates = []

    def add_rates(self, currency):
        self.rates.append(currency)
    
    def get_rates_enconded(self):
        rates = []
        for rate in self.rates:
            rates.append(rate.__dict__)
            pass

        return rates

    def toJson(self):
        # return self.get_rates_enconded()
        return json.dumps({"date": self.date, "base": self.base.value, "rates": self.get_rates_enconded()})



#     {
#         "date": "sdasdsad"
#         "base": {
#             "name": "EUR"
#             "value": "1"
#         }
#         "rates": [
#             {
#                 "name": "BRL"
#                 "value": "121321"
#             }
#         ]
#     }