# **Object oriented programming**

<img src="img/python.gif&ct=s" height="150" alt="Python">

### **Short annotation to the course:**

The purpose of the course is to form the student's knowledge of designing and developing software using the object-oriented programming paradigm.

The course examines the principles of object-oriented programming (encapsulation, inheritance, polymorphism), the need for an optimal balance between imitation and
composition, specifics of using abstract classes and interfaces, elements of object-oriented analysis and design, principles of DRY, KISS, SOLID and templates
designing. The Python programming language and PyCharm integrated development environment are used in the course to create object-oriented computer programs.

---

## **Lab 1**

### **Main**

**📅 Date:** 11.10.2022

**📁 Project:** [link](main-01/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Create a rational class to perform arithmetic operations with rational numbers. Use the \_\_init\_\_() default method for the initialization of attributes of the class - numerator and denominator. The rational number in memory should be stored in a shortened form, for example, a fraction of 2/4 should be stored as 1 in the numerator and 2 in the denominator. Provide the possibility of eliminating rational numbers in A/B format, where a is the numerator, b is the denominator and in floating coma format.

   To demonstrate the Rational Class functionality, create a console application.

2. Create Rectangle class. To initialize attributes-donated classes-the length and width of the rectangle-use the method \_\_init\_\_() with the default arguments. Provide the possibility of determining the perimeter and the area of ​​the rectangle. Access to attributes should be controlled (the length and width of the rectangle should be limited to 100 cm). To demonstrate rectangle functionality, create a console application.

</details>

### **Additional**

**📅 Date:** 11.10.2022

**📁 Project:** [link](additional-01/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

| Attributes 1 and 2             | Method_1 attributes processing     | Method_2 attributes processing                                                           |
| ------------------------------ | ---------------------------------- | ---------------------------------------------------------------------------------------- |
| Book price and number of pages | Increase the number of pages by 10 | Reduce the book price 2 times if its number of pages (after increasing) is more than 200 |

</details>

---

## **Lab 2**

### **Main**

**📅 Date:** 20.10.2022

**📁 Project:** [link](main-02/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1.  RPG-game enables the player to choose the race of the hero: Argonianin, Bretonets, Altmer, Nord, Danmer, Kadjit. In addition to choosing a race, the user has the ability to adjust the appearance of the selected hero: gender, skin color, body weight, tattoos, hair color (if it exists). Write the program to display all the characteristics of the created hero.
2.  Create a Python program to display the active status of the IT project. Each project has its own unique number, which is generated at the stage of the project. The company offers three types of project implementation: standard project, 10 days project and investors project. The project for 10 days has a mark of 60% of the total cost of the project, and the "project for investors" provides a 20% discount for the customer, if it is an investor of the company. Provided that the time is discussed, the company carries losses - 5% of the cost of the project for each overdue week.

    The program must provide the user with the following functionality:

    - display of projects by numbers;

    - reflection of the type of project implementation and its cost at present;

    - all project information should be stored without losing data when leaving the program.

</details>

---

### **Practice 1**

**📅 Date:** 08.10.2022

**📁 Project:** [link](practice-01/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1.  Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc. Determine the required attributes-data and attributes-methods in class for working with the text file.

2.  Write a program for selling tickets to IT-events. Each ticket has a unique number and a price. There are four types of tickets: regular ticket, advance ticket (purchased 60 or more days before the event), late ticket (purchased fewer than 10 days before the event) and student ticket.

    Additional information:
    _ advance ticket - discount 40% of the regular ticket price;
    _ student ticket - discount 50% of the regular ticket price; \* late ticket - additional 10% to the regular ticket price.

    All tickets must have the following properties:

    - the ability to construct a ticket by number;
    - the ability to ask for a ticket’s price;
    - the ability to print a ticket as a String.

</details>

---

## **Controls**

### **Control 1**

**📅 Date:** 14.10.2022

**📁 Project:** [link](control-01/main.py)

<details>
<summary><b>📋 Specification:</b></summary>

1. Develop a class with weather data: date, average temperature, atmospheric pressure, precipitation. Determine the designers, methods/properties of installation and reading of data field values. Determine the days with the highest pressure drop.

2. Create a date of date with fields in closed frequent: day (1-31), month (1-12), year (integer). The class has a designer, methods of setting a day, month and year, methods of obtaining values ​​of day, month and year, as well as two methods of output by templates: "February 12, 2020" and "12.02.2020". Methods for installing class fields should check the correctness of the set parameters.

</details>
