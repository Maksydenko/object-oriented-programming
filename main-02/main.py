from datetime import datetime, date
from random import randint
from json import dump, load, loads


# Task 1

# Appearance

class BaseAppearance:
    def __init__(self, sex, weight, skin_color, tattoo, hair_color=None):
        if sex.lower() != "man" and sex.lower() != "woman":
            raise ValueError("Incorrect sex!")

        if weight <= 0:
            raise "Incorrect weight!"
        self.sex = sex
        self.weight = weight
        self.skin_color = skin_color
        self.tattoo = tattoo

        try:
            super().__init__(hair_color)
        except:
            self.hair_color = None


    def add_appearance(self):
        base_appearance = f"Race: {self.__class__.__name__}, " \
                          f"sex: {self.sex}, weight: {self.weight}, " \
                          f"skin color: {self.skin_color}, " \
                          f"tattoo: {self.tattoo}"

        if self.hair_color != None:
            base_appearance += f"; hair color: {self.hair_color}"
        return base_appearance


class HairColor:
    def __init__(self, hair_color):
        self.hair_color = hair_color


    def add_hair_color(self):
        return self.hair_color


# Races

class Argonianine(BaseAppearance):
    def __str__(self):
        return f"{self.add_appearance()}"


class Breton(BaseAppearance, HairColor):
    def __str__(self):
        return f"{self.add_appearance()}"


class Altmer(BaseAppearance, HairColor):
    def __str__(self):
        return f"{self.add_appearance()}"


class North(BaseAppearance, HairColor):
    def __str__(self):
        return f"{self.add_appearance()}"


class Dunmer(BaseAppearance, HairColor):
    def __str__(self):
        return f"{self.add_appearance()}"


class Kajit(BaseAppearance, HairColor):
    def __str__(self):
        return f"{self.add_appearance()}"


# Task 2

class BaseProject:
    def __init__(self, deadline):
        self.deadline = datetime.strptime(deadline, "%d.%m.%Y").date()

        # Project id generation
        while True:
            id = randint(10000, 99999)

            try:
                with open(f"{id}.json") as project_file:
                    continue
            except:
                self.id = id
                break

        # Default price
        self.price = 1000


    # Price depending on the type of project
    def check_type(self):
        if self.__class__.__name__ == "TenDaysProject":
            self.price *= 1.6

        if self.__class__.__name__ == "InvestorsProject":
            self.price *= 0.8
        return self.price


    # Generate JSON with project information
    def write_json(self):
        project_info = {
            "project type": self.__class__.__name__,
            "deadline": str(self.deadline),
            "price": self.check_type()
        }
        with open(f"{self.id}.json", "w") as project_json:
            dump(project_info, project_json)
            return "Project added"


    # Find a project by ID and find out the current price
    def find_project(self, id):
        try:
            with open(f"{id}.json") as project_json:
                read_file = load(project_json)
                print(f"Project type: {read_file['project type']}; "
            f"current price: "
            f"{self.check_terms(read_file['deadline'], read_file['price'])}")
        except:
            print("Project not found")


    # Price depending on overdue weeks
    @staticmethod
    def check_terms(deadline, price):
        # Days passed from the deadline to the release of the project
        days_difference = (date.today() -
                           datetime.strptime(deadline,
                                             "%Y-%m-%d").date()).days

        # Overdue weeks
        weeks = days_difference // 7

        if weeks >= 20:
            return 0

        if weeks > 0:
            discount = 5
            discount *= weeks
            price *= 1 - discount / 100
        return price


# Project types

class StandartProject(BaseProject):
    def __str__(self):
        return f"{self.write_json()}"


class TenDaysProject(BaseProject):
    def __str__(self):
        return f"{self.write_json()}"


class InvestorsProject(BaseProject):
    def __str__(self):
        return f"{self.write_json()}"
