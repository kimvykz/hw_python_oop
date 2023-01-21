import datetime as dt

date_format = '%d.%m.%Y'
today_ = dt.datetime.now()
today_str_ = today_.strftime(date_format)

class Record:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        self.date = date

    

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        records = []


class CaloriesCalculator(Calculator):
    
    ate_food_ = []

    def add_record(self, something):
        res_ = [something.amount, something.comment, something.date]
        self.ate_food_.append(res_)


    def get_calories_remained(self):
        res_ = ''
        ate_sum_ = 0

        for food_ in self.ate_food_:
            if food_[2] == today_str_:
                ate_sum_ += food_[0]

        if ate_sum_ < self.limit:
            res_ = f'Сегодня можно съесть что-нибудь ещё, но c общей калорийностью не более {self.limit - ate_sum_} кКал'
        else:
            res_ = 'Хватит есть!'

        return res_


class CashCalculator(Calculator):
    
    transactions_ = []

    def add_record(self, someone):
        res_ = [someone.amount, someone.comment, someone.date]
        #print(res_)
        self.transactions_.append(res_)


    def get_today_cash_remained(self, currency):
        self.currency = currency
        
        res_ = ''
        spent = 0
        #print(today_str_)

        for list_ in self.transactions_:
            if list_[2] == today_str_:
                spent += list_[0]
            
        #print(spent)

        if spent < self.limit:
            res_ = f'На сегодня осталось {self.limit - spent} {currency}'
        elif spent == self.limit:
            res_ = f'Денег нет, держись'
        else:
            res_ = f'Денег нет, держись: твой долг - {self.limit - spent} {currency}'
        return res_



cash_calculator = CashCalculator(1000)
cal_calculator = CaloriesCalculator(2000)

cash_calculator.add_record(Record(150,'coffe','21.01.2023'))
cash_calculator.add_record(Record(75,'tea','19.01.2023'))
cash_calculator.add_record(Record(700,'dinner','21.01.2023'))
cash_calculator.add_record(Record(50,'lunch','21.01.2023'))

cal_calculator.add_record(Record(500,'salad','21.01.2023'))
cal_calculator.add_record(Record(700,'pelmeni','21.01.2023'))
cal_calculator.add_record(Record(600,'shashlyq','21.01.2023'))



print(cash_calculator.get_today_cash_remained('KZT'))
print(cal_calculator.get_calories_remained())

#print(cash_calculator.transactions_)
         