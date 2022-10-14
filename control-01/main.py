# Task 1

class Weather:

    def __init__(self, date, temperature, pressure, precipitation):
        self.day = [date, temperature, pressure, precipitation]
        Weather.add_day(self.day)

    list_days = []

    @classmethod
    def add_day(cls, day):
        return cls.list_days.append(day)


    def check_pressure(self):
        days = Weather.list_days
        number_day = 0
        max_pressure = 0
        for count_day in range(len(days)):
            if days[count_day][2] > max_pressure:
                max_pressure = days[count_day][2]
                number_day = count_day
        return days[number_day]


    def __str__(self):
        return f"{self.check_pressure()[0]} temperature " \
               f"{self.check_pressure()[1]} degrees Celsius, atmospheric " \
               f"pressure {self.check_pressure()[2]} mmHg, " \
               f"chance of precipitation {self.check_pressure()[3]}%"


# Task 2

class Date:

    def get_date(self):
        from datetime import datetime, date

        return date.today()


    def write_date(self):
        return self.get_date().strftime("%d %B %Y")
