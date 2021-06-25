from currency import CurrencyType
from currency import Currency
from currency import CurrencyRate
from euro_scrapper import EuroScrapper
import json


class Euro(): 

    def __init__(self):
        self.scrapper = EuroScrapper()
        self.currencyRate = CurrencyRate(CurrencyType.EURO)

    def add_currency(self, currencyType):

        if currencyType == CurrencyType.REAL:
            brl = self.scrapper.get_brl()
            self.currencyRate.rates.append(Currency(currencyType.value, brl))

    def toJson(self):
        return self.currencyRate.toJson()
