from datetime import datetime


# Task 1

class Weather:

    def __init__(self, date, temperature, pressure, precipitation):
        if datetime.strptime(date, "%d.%m.%Y") and pressure > 0 \
                and 0 <= precipitation <= 100:
            self.day = [date, temperature, pressure, precipitation]
            Weather.list_days.append(self.day)
        else:
            raise ValueError("Atmospheric pressure must be greater than "
                             "0 mmHg, and the probability of precipitation from 0 to 100%")

    list_days = []

    def check_pressure(self):
        days = Weather.list_days
        max_days = []
        max_pressure = 0

        for count_day in range(len(days)):
            if days[count_day][2] > max_pressure:
                max_pressure = days[count_day][2]

        for count_day in range(len(days)):
            if days[count_day][2] == max_pressure:
                max_days.append(days[count_day])
        # print(max_days)
        return max_days

    def __str__(self):
        for count_day in range(days):
            print(f"{self.check_pressure()[count_day][0]} temperature "
                  f"{self.check_pressure()[count_day][1]} "
                  f"degrees Celsius, atmospheric pressure "
                  f"{self.check_pressure()[count_day][2]} mmHg, chance of "
                  f"precipitation {self.check_pressure()[count_day][3]}%")
        return "↑ Days with the highest barometric pressure ↑"


# Task 2

class Date:

    def __init__(self, day_date, month=0, year=0):
        self.day_date = day_date
        self.month = month
        self.year = year

    def change_format(self):
        number_date = "%d.%m.%Y"
        word_date = "%d %B %Y"

        if self.month == 0 and self.year == 0:
            date = datetime.strptime(self.day_date, number_date)
            return date.strftime(word_date)
        string_date = str(self.day_date) + " " + self.month + " " + str(self.year)
        date = datetime.strptime(string_date, word_date)
        return date.strftime(number_date)

    def __str__(self):
        return f"{self.change_format()}"
