#################################################
#  
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON 
# 👉 Python Class Method
#################################################   


# Python Class Method

# Example 1: Create Class Method Using @classmethod Decorator

from datetime import date

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate age an set it as a age
        # return new object
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))

jessa = Student('Jessa', 20)
jessa.show()

# create new object using the factory method
joy = Student.calculate_age("Joy", 1995)
joy.show()


# Example 2: Create Class Method Using classmethod() function


class School:
    # class variable
    name = 'ABC School'

    def school_name(cls):
        print('School Name is :', cls.name)

# create class method
School.school_name = classmethod(School.school_name)

# call class method
School.school_name()

# Example 3: Access Class Variables in Class Methods

class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, school_name):
        # class_name.class_variable
        cls.school_name = school_name

    # instance method
    def show(self):
        print(self.name, self.age, 'School:', Student.school_name)

jessa = Student('Jessa', 20)
jessa.show()

# change school_name
Student.change_school('XYZ School')
jessa.show()


# Class Method in Inheritance

class Vehicle:
    brand_name = 'BMW'

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_price(cls, name, price):
        # ind_price = dollar * 76
        # create new Vehicle object
        return cls(name, (price * 75))

    def show(self):
        print(self.name, self.price)

class Car(Vehicle):
    def average(self, distance, fuel_used):
        mileage = distance / fuel_used
        print(self.name, 'Mileage', mileage)

bmw_us = Car('BMW X5', 65000)
bmw_us.show()

# class method of parent class is available to child class
# this will return the object of calling class
bmw_ind = Car.from_price('BMW X5', 65000)
bmw_ind.show()

# check type
print(type(bmw_ind))

# Dynamically Add Class Method to a Class

class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

# class ended

# method outside class
def exercises(cls):
    # access class variables
    print("Below exercises for", cls.school_name)

# Adding class method at runtime to class
Student.exercises = classmethod(exercises)

jessa = Student("Jessa", 14)
jessa.show()
# call the new method
Student.exercises()


# Dynamically Delete Class Methods