# Task 1

class Weather:

    def __init__(self, date, temperature, pressure, precipitation):
        self.day = [date, temperature, pressure, precipitation]
        Weather.__add_day(self.day)

    list_days = []

    @classmethod
    def __add_day(cls, day):
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
               f"{self.check_pressure()[1]} degrees Celsius, " \
               f"atmospheric pressure {self.check_pressure()[2]} mmHg, " \
               f"chance of precipitation {self.check_pressure()[3]}%"


# Task 2

class Date:

    def __init__(self, day, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year


    def change_format(self):
        from datetime import datetime, date

        if self.month == 0 or self.year == 0:
            date = datetime.strptime(self.day, "%d.%m.%Y")
            return date.strftime("%d %B %Y")
        date = datetime.strptime(str(self.day) + " " + self.month + " " + str(self.year), "%d %B %Y")
        return date.strftime("%d.%m.%Y")


    def __str__(self):
        return f"{self.change_format()}"
