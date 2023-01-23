import datetime as dt

date_format = '%d.%m.%Y'
today_ = dt.datetime.now().date()
today_str_ = today_.strftime(date_format)
week_dates_list_ = []

for day_ in range(0,7):
    week_dates_list_.append(today_ - dt.timedelta(days=day_))
    

class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.comment = comment
        if date == '':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date,'%d.%m.%Y').date()
        
    

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        #records = []


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)
    
    ate_food_ = []

    def add_record(self, something):
        res_ = [something.amount, something.comment, something.date]
        self.ate_food_.append(res_)


    def get_calories_remained(self):
        res_ = ''
        ate_sum_ = 0

        for food_ in self.ate_food_:
            if food_[2] == today_:
                ate_sum_ += food_[0]

        if ate_sum_ < self.limit:
            res_ = f'Сегодня можно съесть что-нибудь ещё, но c общей калорийностью не более {self.limit - ate_sum_} кКал'
        else:
            res_ = 'Хватит есть!'

        return res_

    def get_today_stats(self):
        res_ = 0
        for today_ate_ in self.ate_food_:
            if today_ate_[2] == today_:
                res_ += today_ate_[0]
        return f'На сегодня употребленно: {res_} кКал'

    def get_week_stats(self):
        res_ = 0

        for food_ in self.ate_food_:
            if food_[2] in week_dates_list_:
                res_ += food_[0]
        return f'За последнюю неделю съедено: {res_} кКал'

class CashCalculator(Calculator):

    KZT_RATE = 1.00
    USD_RATE = 465.00
    EUR_RATE = 505.50

    currencies_ = {
        'KZT' : ('Tenge', KZT_RATE),
        'USD' : ('Dollars', USD_RATE),
        'EUR' : ('Euro', EUR_RATE)
    }

    
    def __init__(self, limit):
        super().__init__(limit)
    
    transactions_ = []

    def add_record(self, someone):
        res_ = [someone.amount, someone.comment, someone.date]
        #print(res_)
        #print(type(someone))
        self.transactions_.append(res_)
        

    def get_today_cash_remained(self, currency):
        self.currency = currency
        
        res_ = ''
        spent = 0
        #print(today_str_)

        for list_ in self.transactions_:
            if list_[2] == today_:
                spent += list_[0]
            
        #print(spent)

        if spent < self.limit:
            res_ = f'На сегодня осталось {round((self.limit - spent)/self.currencies_[currency][1], 2)} {self.currencies_[currency][0]}'
        elif spent == self.limit:
            res_ = f'Денег нет, держись'
        else:
            res_ = f'Денег нет, держись: твой долг - {round((self.limit - spent)/self.currencies_[currency][1], 2)} {self.currencies_[currency][0]}'
        return res_

    def get_today_stats(self, currency):
        res_ = 0

        for today_spent_ in self.transactions_:
            if today_spent_[2] == today_:
                res_ += today_spent_[0]

        return f'На сегодня уже потрачено: {round(res_/self.currencies_[currency][1],2)} {self.currencies_[currency][0]}'

    def get_week_stats(self, currency):   
        res_ = 0

        for spent_ in self.transactions_:
            if spent_[2] in week_dates_list_:
                res_ += spent_[0] 
        return f'За последнюю неделю потрачено {round(res_/self.currencies_[currency][1],2)} {self.currencies_[currency][0]}'


cash_calculator = CashCalculator(1000)
cal_calculator = CaloriesCalculator(2000)

cash_calculator.add_record(Record(150,'coffe','21.01.2023'))
cash_calculator.add_record(Record(75,'tea','19.01.2023'))
cash_calculator.add_record(Record(700,'dinner','21.01.2023'))
cash_calculator.add_record(Record(50,'lunch','21.01.2023'))
cash_calculator.add_record(Record(75,'tea','23.01.2023'))
cash_calculator.add_record(Record(700,'dinner','23.01.2023'))
cash_calculator.add_record(Record(50,'lunch','23.01.2023'))

cal_calculator.add_record(Record(500,'salad','21.01.2023'))
cal_calculator.add_record(Record(700,'pelmeni','21.01.2023'))
cal_calculator.add_record(Record(600,'shashlyq','21.01.2023'))
cal_calculator.add_record(Record(400,'salad','23.01.2023'))
cal_calculator.add_record(Record(900,'pelmeni','23.01.2023'))
cal_calculator.add_record(Record(850,'shashlyq','23.01.2023'))



print(cash_calculator.get_today_cash_remained('KZT'))
print(cal_calculator.get_calories_remained())
print(cal_calculator.get_today_stats())
print(cash_calculator.get_today_stats('USD'))
print(cal_calculator.get_week_stats())
print(cash_calculator.get_week_stats('EUR'))

#print(cash_calculator.transactions_)
         