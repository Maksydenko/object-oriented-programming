from datetime import datetime


# Task 1
class Weather:
    def __init__(self, date, temperature, pressure, precipitation):
        if datetime.strptime(date, "%d.%m.%Y") and pressure > 0 \
                and 0 <= precipitation <= 100:
            self.day = {"date": date, "temperature": temperature,
                        "pressure": pressure, "precipitation": precipitation}
            Weather.list_days.append(self.day)
        else:
            raise ValueError(
                "Atmospheric pressure must be greater than 0 mmHg, and the probability of precipitation from 0 to 100%")

    list_days = []

    def check_pressure(self):
        days = Weather.list_days
        pressure = "pressure"
        max_pressure = 0

        for count_days in range(len(days)):
            if days[count_days][pressure] > max_pressure:
                max_pressure = days[count_days][pressure]

        max_days = []

        for count_days in range(len(days)):
            if days[count_days][pressure] == max_pressure:
                max_days.append(days[count_days])
        return max_days

    def __str__(self):
        max_days = self.check_pressure()

        for count_days in range(len(max_days)):
            print(f"{max_days[count_days]['date']} temperature "
                  f"{max_days[count_days]['temperature']} degrees Celsius, "
                  f"atmospheric pressure {max_days[count_days]['pressure']}"
                  f" mmHg, chance of precipitation "
                  f"{max_days[count_days]['precipitation']}%")
        return "↑ days with the highest barometric pressure ↑"


# Task 2
class Date:
    def __init__(self, *args):
        if len(args) == 1:
            self.date = args[0]
        elif len(args) == 3:
            self.month = args[0]
            self.day = args[1]
            self.year = args[2]
        else:
            raise ValueError("You wrote too few or too many arguments")

    def change_format(self):
        number_date = "%d.%m.%Y"
        word_date = "%B %d, %Y"

        try:
            date = datetime.strptime(self.date, number_date)
            return date.strftime(word_date)
        except:
            string_date = self.month + " " + str(self.day) + ", " \
                + str(self.year)
            date = datetime.strptime(string_date, word_date)
            return date.strftime(number_date)

    def __str__(self):
        return f"{self.change_format()}"
