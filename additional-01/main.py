class Book:

    def __init__(self, book_value, pages_number):
        if book_value or pages_number <= 0:
            raise ValueError("Wrong value of book or number of pages!")
        self.book_value = book_value
        self.pages_number = pages_number


    def __add_pages(self):
        return self.pages_number + 10


    def __get_price(self):
        if self.__add_pages() > 200:
            return self.book_value / 2
        return self.book_value


    def __str__(self):
        return f"Value of book: ${self.__get_price()}"