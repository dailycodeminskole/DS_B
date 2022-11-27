  
#################################################
#  
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON 
# 👉 Instance Variables  PYTHON 
#################################################
# Python Instance Variables

# What is an Instance Variable in Python?

# If the value of a variable varies from object to object, then such variables are called instance variables. For every object, a separate copy of the instance variable will be created.

# We can access the instance variable using the object and dot (.) operator.


# Create Instance Variables

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create first object
s1 = Student("Jessa", 20)

# access instance variable
print('Object 1')
print('Name:', s1.name)
print('Age:', s1.age)

# create second object
s2= Student("Kelly", 10)

# access instance variable
print('Object 2')
print('Name:', s2.name)
print('Age:', s2.age)


# Modify Values of Instance Variables
class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
stud = Student("Jessa", 20)

print('Before')
print('Name:', stud.name, 'Age:', stud.age)

# modify instance variable
stud.name = 'Emma'
stud.age = 15

print('After')
print('Name:', stud.name, 'Age:', stud.age)

# Ways to Access Instance Variable

# There are two ways to access the instance variable of class:

        # Within the class in instance method by using the object reference (self)
        # Using getattr() method


# Example 1: Access instance variable in the instance method

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method access instance variable
    def show(self):
        print('Name:', stud.name, 'Age:', stud.age)

# create object
stud = Student("Jessa", 20)

# call instance method
stud.show()


# Example 2: Access instance variable using getattr()

# getattr(Object, 'instance_variable')

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
stud = Student("Jessa", 20)

# Use getattr instead of stud.name
print('Name:', getattr(stud, 'name'))
print('Age:', getattr(stud, 'age'))


# Dynamically Add Instance Variable to a Object

class Student:
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
stud = Student("Jessa", 20)

print('Before')
print('Name:', stud.name, 'Age:', stud.age)

# add new instance variable 'marks' to stud
stud.marks = 75
print('After')
print('Name:', stud.name, 'Age:', stud.age, 'Marks:', stud.marks)


# Access Instance Variable From Another Class

class Vehicle:
    def __init__(self):
        self.engine = '1500cc'

class Car(Vehicle):
    def __init__(self, max_speed):
        # call parent class constructor
        super().__init__()
        self.max_speed = max_speed

    def display(self):
        # access parent class instance variables 'engine'
        print("Engine:", self.engine)
        print("Max Speed:", self.max_speed)

# Object of car
car = Car(240)
car.display()


# List all Instance Variables of a Object

class Student:
    def __init__(self, roll_no, name):
        # Instance variable
        self.roll_no = roll_no
        self.name = name

s1 = Student(10, 'Jessa')
print('Instance variable object has')
print(s1.__dict__)

# Get each instance variable
for key_value in s1.__dict__.items():
    print(key_value[0], '=', key_value[1])


