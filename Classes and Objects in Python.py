 #################################################
#  
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON 
# 👉 Classes and Objects in Python 
#################################################






# What is a Class and Objects in Python?
# Class: The class is a user-defined data structure that binds the data members and methods into a single unit. Class is a blueprint or code template for object creation. Using a class, you can create as many objects as you want.
# Object: An object is an instance of a class. It is a collection of attributes (variables) and methods. We use the object of a class to perform actions.
# Objects have two characteristics: They have states and behaviors (object has attributes and methods attached to it) Attributes represent its state, and methods represent its behavior. Using its methods, we can modify its state.

# In short, Every object has the following property.

# Identity: Every object must be uniquely identified.
# State: An object has an attribute that represents a state of an object, and it also reflects the property of an object.
# Behavior: An object has methods that represent its behavior.


# Python is an Object-Oriented Programming language, so everything in Python is treated as an object. An object is a real-life entity. It is the collection of various data and functions that operate on those data.



# A real-life example of class and objects.

# Class: Person

# State: Name, Sex, Profession
# Behavior: Working, Study


# Create a Class in Python

# Syntax

# class class_name:
#     '''This is a docstring. I have created a new class'''
#     <statement 1>
#     <statement 2>
#     .
#     .
#     <statement N>




class Person:
    def __init__(self, name, sex, profession):
        # data members (instance variables)
        self.name = name
        self.sex = sex
        self.profession = profession

    # Behavior (instance methods)
    def show(self):
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    # Behavior (instance methods)
    def work(self):
        print(self.name, 'working as a', self.profession)


# An object is essential to work with the class attributes. The object is created using the class name. When we create an object of the class, it is called instantiation. The object is also called the instance of a class.



# create object of a class
jessa = Person('Jessa', 'Female', 'Software Engineer')

# call methods
jessa.show()
jessa.work()


# In Class, 
# attributes can be defined into two parts:

# Instance variables: The instance variables are attributes attached to an instance of a class. We define instance variables in the constructor ( the __init__() method of a class).
# Class Variables: A class variable is a variable that is declared inside of class, but outside of any instance method or __init__() method.



class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

s1 = Student("Harry", 12)
# access instance variables
print('Student:', s1.name, s1.age)

# access class variable
print('School name:', Student.school_name)

# Modify instance variables
s1.name = 'Jessa'
s1.age = 14
print('Student:', s1.name, s1.age)

# Modify class variables
Student.school_name = 'XYZ School'
print('School name:', Student.school_name)


# In Object-oriented programming, Inside a Class, we can define the following three types of methods.

# Instance method: Used to access or modify the object state. If we use instance variables inside a method, such methods are called instance methods.
# Class method: Used to access or modify the class state. In method implementation, if we use only class variables, then such type of methods we should declare as a class method.
# Static method: It is a general utility method that performs a task in isolation. Inside this method, we don’t use instance or class variable because this static method doesn’t have access to the class attributes.


# class methods demo
class Student:
    # class variable
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance method
    def show(self):
        # access instance variables and class variables
        print('Student:', self.name, self.age, Student.school_name)

    # instance method
    def change_age(self, new_age):
        # modify instance variable
        self.age = new_age

    # class method
    @classmethod
    def modify_school_name(cls, new_name):
        # modify class variable
        cls.school_name = new_name

s1 = Student("Harry", 12)

# call instance methods
s1.show()
s1.change_age(14)

# call class method
Student.modify_school_name('XYZ School')
# call instance methods
s1.show()
