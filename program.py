import datetime as dt

date_format = '%d.%m.%Y'
today_ = dt.datetime.now()
today_str_ = today_.strftime(date_format)
week_dates_list_ = []

for day_ in range(0,7):
    week_dates_list_.append((today_ - dt.timedelta(days=day_)).strftime(date_format))
    

class Record:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        self.date = date
    

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        #records = []


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

    def get_today_stats(self):
        res_ = 0
        for today_ate_ in self.ate_food_:
            if today_ate_[2] == today_str_:
                res_ += today_ate_[0]
        return f'На сегодня употребленно: {res_} кКал'

    def get_week_stats(self):
        res_ = 0

        for food_ in self.ate_food_:
            if food_[2] in week_dates_list_:
                res_ += food_[0]
        return f'За последнюю неделю съедено: {res_} кКал'

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

    def get_today_stats(self):
        res_ = 0

        for today_spent_ in self.transactions_:
            if today_spent_[2] == today_str_:
                res_ += today_spent_[0]

        return f'На сегодня уже потрачено: {res_} {self.currency}'

    def get_week_stats(self):   
        res_ = 0

        for spent_ in self.transactions_:
            if spent_[2] in week_dates_list_:
                res_ += spent_[0] 
        return f'За последнюю неделю потрачено {res_} {self.currency}'


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
print(cash_calculator.get_today_stats())
print(cal_calculator.get_week_stats())
print(cash_calculator.get_week_stats())

#print(cash_calculator.transactions_)
         