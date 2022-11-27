 
#################################################
#  
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON 
#################################################
#  Encapsulation in Python


# Encapsulation in Python
# Need for Encapsulation
# Data Hiding using public, protected, and private members
# Data Hiding vs. Encapsulation
# Getter and Setter Methods
# Benefits of Encapsulation

# A class is an example of encapsulation as it binds all the data members (instance variables) and methods into a single unit.

# Example

class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.project)

# creating object of a class
emp = Employee('Jessa', 8000, 'NLP')

# calling public method of the class
emp.show()
emp.work()


# Using encapsulation, we can hide an object’s internal representation from the outside. This is called information hiding.


# Access Modifiers in Python
# Encapsulation can be achieved by declaring the data members and methods of a class either as private or protected. 

# Access modifiers limit access to the variables and methods of a class. Python provides three types of access modifiers private, public, and protected.

# Public Member: Accessible anywhere from otside oclass.
# Private Member: Accessible within the class
# Protected Member: Accessible within the class and its sub-classes

# Public Member
# Example

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data members
        self.name = name
        self.salary = salary

    # public instance methods
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

# creating object of a class
emp = Employee('Jessa', 10000)

# accessing public data members
print("Name: ", emp.name, 'Salary:', emp.salary)

# calling public method of the class
emp.show()



# Private Member
# To define a private variable add two underscores as a prefix at the start of a variable name.

# Private members are accessible only within the class, and we can’t access them directly from the class objects.


# Example
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Jessa', 10000)

# accessing private data members
print('Salary:', emp.__salary)




# We can access private members from outside of a class using the following two approaches

# Create public method to access private members
        # Use name mangling
        # Public method to access private members

# Example
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

# creating object of a class
emp = Employee('Jessa', 10000)

# calling public method of the class
emp.show()


#Name Mangling to access private members

# Example

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Jessa', 10000)

print('Name:', emp.name)
# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)


# 
# Protected Member

# Protected members are accessible within the class and also available to its sub-classes. To define a protected member, prefix the member name with a single underscore _.

# Protected data members are used when you implement inheritance and want to allow data members access to only child classes.

# Example: Proctecd member in inheritance.

# base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"

# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()

# Direct access protected data member
print('Project:', c._project)


#Getters and Setters in Python
# To implement proper encapsulation in Python, we need to use setters and getters. The primary purpose of using getters and setters in object-oriented programs is to ensure data encapsulation. Use the getter method to access data members and the setter methods to modify the data members.

# The getters and setters methods are often used when:
# When we want to avoid direct access to private variables
# To add validation logic for setting a value


# Example

class Student:
    def __init__(self, name, age):
        # private member
        self.name = name
        self.__age = age

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, age):
        self.__age = age

stud = Student('Jessa', 14)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())

# changing age using setter
stud.set_age(16)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())


# Example: Information Hiding and conditional logic for setting an object attributes

class Student:
    def __init__(self, name, roll_no, age):
        # private member
        self.name = name
        # private members to restrict access
        # avoid direct data modification
        self.__roll_no = roll_no
        self.__age = age

    def show(self):
        print('Student Details:', self.name, self.__roll_no)

    # getter methods
    def get_roll_no(self):
        return self.__roll_no

    # setter method to modify data member
    # condition to allow data modification with rules
    def set_roll_no(self, number):
        if number > 50:
            print('Invalid roll no. Please set correct roll number')
        else:
            self.__roll_no = number

jessa = Student('Jessa', 10, 15)

# before Modify
jessa.show()
# changing roll number using setter
jessa.set_roll_no(120)


jessa.set_roll_no(25)
jessa.show()



# Advantages of Encapsulation
# Security: The main advantage of using encapsulation is the security of the data. Encapsulation protects an object from unauthorized access. It allows private and protected access levels to prevent accidental data modification.
# Data Hiding: The user would not be knowing what is going on behind the scene. They would only be knowing that to modify a data member, call the setter method. To read a data member, call the getter method. What these setter and getter methods are doing is hidden from them.
# Simplicity: It simplifies the maintenance of the application by keeping classes separated and preventing them from tightly coupling with each other.
# Aesthetics: Bundling data and methods within a class makes code more readable and maintainable