# Task 1

class InfoTxt:

    def __init__(self, path_file):
        self.path_file = path_file
        self.__line_count = 0
        self.__word_count = 0
        self.__symbol_count = 0

        try:
            with open(self.path_file) as file:
                self.__text_list = file.readlines()
                file.seek(0)
                self.__text = file.read()
        except FileNotFoundError as fnfe:
            print(fnfe)


    def count_lines(self):
        self.__line_count = len(self.__text_list)
        return self.__line_count


    def count_words(self):
        for line in self.__text_list:
            self.__word_count += len(line.split())
        return self.__word_count


    def count_symbols(self):
        self.__symbol_count = len(self.__text.replace("\n", ""))
        return self.__symbol_count


    def __str__(self):
        return f"In file {self.count_lines()} lines, " \
               f"{self.count_words()} words, {self.count_symbols()} symbols"

# Task 2

class Ticket:

    def __init__(self, ticket_number, event_date, age):
        self.ticket_number = ticket_number
        self.event_date = event_date
        self.age = age
        self.__ticket_price = 10


    def __check_price(self):
        from datetime import datetime, date


        days_difference = (datetime.strptime(self.event_date,
                          '%d.%m.%Y').date() - date.today()).days

        if days_difference < 0:
            return -1
        else:
            if 15 <= self.age <= 23:
                self.__ticket_price *= 0.5
                return self.__ticket_price
            else:
                if days_difference >= 60:
                    self.__ticket_price *= 0.6
                    return self.__ticket_price
                if days_difference <= 10:
                    self.__ticket_price *= 1.1
                    return self.__ticket_price


    def __str__(self):
        if self.age < 0:
            return "Wrong age!"
        if self.__check_price() == -1:
            return "Impossible to buy a ticket! The event has already started"
        return f"Number of your ticket: {self.ticket_number}, price: {self.__ticket_price}$"
