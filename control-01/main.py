# Task 1

class Weather:

    def __init__(self, date, temperature, pressure, precipitation):
        self.day = [date, temperature, pressure, precipitation]
        Weather.add_day(self.day)

    days_list = []

    @classmethod
    def add_day(cls, day):
        return cls.days_list.append(day)


    def check_pressure(self):
        number_day = 0
        max_pressure = 0
        for i in range(len(Weather.days_list)):
            if Weather.days_list[i][2] > max_pressure:
                max_pressure = Weather.days_list[i][2]
                number_day = i
        return Weather.days_list[number_day]


    def __str__(self):
        return self.check_pressure()


# Task 2

class Date:

    def get_date(self):
        from datetime import datetime, date

        return date.today()


    def write_date(self):
        return self.get_date().strftime("%d %B %Y")
