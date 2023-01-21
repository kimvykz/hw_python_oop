import datetime as dt

date_format = '%d.%m.%Y'

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        records = []


class CaloriesCalculator(Calculator):
    
    def get_calories_remained(self):
        lim_ = 0
        res_ = ''

        if lim_ > 100:
            res_ = f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {lim_} кКал'
        else:
            res_ = 'Хватит есть!'

        return res_


class CashCalculator(Calculator):

    def get_today_cash_remained(self, currency):
        self.currency = currency
        limit = 100
        spent = 59
        res_
        if spent > limit:
            res_ = f'На сегодня осталось N руб/USD/Euro'
        elif spent == limit:
            res_ = f'Денег нет, держись'
        else:
            res_ = f'Денег нет, держись: твой долг - N руб/USD/Euro'
        return res_



class Record:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        self.date = date

    def add_record():
        return ''

transactions = {
    '2023-01-21' : 123
                }

print('Everything is OK!')    
print(dt.datetime.now().date())            