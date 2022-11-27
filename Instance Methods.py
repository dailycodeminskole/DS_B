#################################################
#  
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON 
# 👉 Python Instance Methods
#################################################

# Instance Methods

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method to access instance variable
    def show(self):
        print('Name:', self.name, 'Age:', self.age)



# Calling An Instance Method

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method access instance variable
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

# create first object
print('First Student')
emma = Student("Jessa", 14)
# call instance method
emma.show()

# create second object
print('Second Student')
kelly = Student("Kelly", 16)
# call instance method
kelly.show()

# By Using self.__class__ attribute we can access the class attributes and change the class state. Therefore instance method gives us control of changing the object as well as the class state.

# Modify Instance Variables inside Instance Method

class Student:
    def __init__(self, roll_no, name, age):
        # Instance variable
        self.roll_no = roll_no
        self.name = name
        self.age = age

    # instance method access instance variable
    def show(self):
        print('Roll Number:', self.roll_no, 'Name:', self.name, 'Age:', self.age)

    # instance method to modify instance variable
    def update(self, roll_number, age):
        self.roll_no = roll_number
        self.age = age

# create object
print('class VIII')
stud = Student(20, "Emma", 14)
# call instance method
stud.show()

# Modify instance variables
print('class IX')
stud.update(35, 15)
stud.show()


# Create Instance Variables in Instance Method

# Till the time we used constructor to create instance attributes. But, instance attributes are not specific only to the __init__() method; they can be defined elsewhere in the class. So, let’s see how to create an instance variable inside the method.

class Student:
    def __init__(self, roll_no, name, age):
        # Instance variable
        self.roll_no = roll_no
        self.name = name
        self.age = age

    # instance method to add instance variable
    def add_marks(self, marks):
        # add new attribute to current object
        self.marks = marks

# create object
stud = Student(20, "Emma", 14)
# call instance method
stud.add_marks(75)

# display object
print('Roll Number:', stud.roll_no, 'Name:', stud.name, 'Age:', stud.age, 'Marks:', stud.marks)




# Dynamically Add Instance Method to a Object

# We should add a method to the object, so other instances don’t have access to that method. We use the types module’s MethodType() to add a method to an object. Below is the simplest way to method to an object.

import types

class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

# create new method
def welcome(self):
    print("Hello", self.name, "Welcome to Class IX")


# create object
s1 = Student("Jessa", 15)

# Add instance method to object
s1.welcome = types.MethodType(welcome, s1)
s1.show()

# call newly added method
s1.welcome()


# Dynamically Delete Instance Methods
        # By using the del operator
        # By using delattr() method

# By using the del operator
class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

    # instance method
    def percentage(self, sub1, sub2):
        print('Percentage:', (sub1 + sub2) / 2)

emma = Student('Emma', 14)
emma.show()
emma.percentage(67, 62)

# Delete the method from class using del operator
del emma.percentage

# Again calling percentage() method
# It will raise error
emma.percentage(67, 62)


# By using delattr() method
# delattr(object, name)

emma = Student('Emma', 14)
emma.show()
emma.percentage(67, 62)

# delete instance method percentage() using delattr()
delattr(emma, 'percentage')
emma.show()

# Again calling percentage() method
# It will raise error
emma.percentage(67, 62)