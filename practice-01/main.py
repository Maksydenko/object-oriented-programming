# Task 1

class InfoTxt:

    def __init__(self, path_file):
        try:
            with open(path_file) as file:
                self.__text_list = file.readlines()
                file.seek(0)
                self.__text = file.read()
        except FileNotFoundError as fnfe:
            print(fnfe)


    def count_lines(self):
        return len(self.__text_list)


    def count_words(self):
        word_count = 0

        for line in self.__text_list:
            word_count += len(line.split())
        return word_count


    def count_symbols(self):
        return len(self.__text.replace("\n", ""))


    def __str__(self):
        return f"In file {self.count_lines()} lines, " \
               f"{self.count_words()} words, {self.count_symbols()} symbols"


# Task 2

class Ticket:

    def __init__(self, ticket_number, event_date, age):
        self.age = age
        self.days_difference = self.check_date(event_date)

        if self.age and self.days_difference >= 0:
            self.ticket_number = ticket_number


    def __get_price(self):
        ticket_price = 10

        if 15 <= self.age <= 23:
            return ticket_price * 0.5
        else:
            if self.days_difference >= 60:
                return ticket_price * 0.6
            if self.days_difference <= 10:
                return ticket_price * 1.1
            else:
                return ticket_price


    @staticmethod
    def check_date(event_date):
        from datetime import datetime, date

        return (datetime.strptime(event_date,
                "%d.%m.%Y").date() - date.today()).days


    def __str__(self):
        if self.age < 0:
            raise ValueError("Wrong age!")
        if self.days_difference < 0:
            raise ValueError("Impossible to buy a ticket! The event has already started")
        return f"Number of your ticket: {self.ticket_number}, price: {self.__get_price()} $"