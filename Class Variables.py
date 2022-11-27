#################################################
#  
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON 
# 👉 Python Class Variables
#################################################
# Python Class Variables

# Create Class Variables
class Student:
    # Class variable
    school_name = 'ABC School '
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

# create first object
s1 = Student('Emma', 10)
print(s1.name, s1.roll_no, Student.school_name)
# access class variable

# create second object
s2 = Student('Jessa', 20)
# access class variable
print(s2.name, s2.roll_no, Student.school_name)


# Example 1: Access Class Variable in the constructor

class Student:
    # Class variable
    school_name = 'ABC School '

    # constructor
    def __init__(self, name):
        self.name = name
        # access class variable inside constructor using self
        print(self.school_name)
        # access using class name
        print(Student.school_name)

# create Object
s1 = Student('Emma')

# Example 2: Access Class Variable in Instance method and outside class

class Student:
    # Class variable
    school_name = 'ABC School '

    # constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Instance method
    def show(self):
        print('Inside instance method')
        # access using self
        print(self.name, self.roll_no, self.school_name)
        # access using class name
        print(Student.school_name)

# create Object
s1 = Student('Emma', 10)
s1.show()

print('Outside class')
# access class variable outside class
# access using object reference
print(s1.school_name)

# access using class name
print(Student.school_name)



# Modify Class Variables

class Student:
    # Class variable
    school_name = 'ABC School '

    # constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Instance method
    def show(self):
        print(self.name, self.roll_no, Student.school_name)

# create Object
s1 = Student('Emma', 10)
print('Before')
s1.show()

# Modify class variable
Student.school_name = 'XYZ School'
print('After')
s1.show()

# It is best practice to use a class name to change the value of a class variable. Because if we try to change the class variable’s value by using an object, a new instance variable is created for that particular object, which shadows the class variables.


class Student:
    # Class variable
    school_name = 'ABC School '

    # constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

# create Objects
s1 = Student('Emma', 10)
s2 = Student('Jessa', 20)

print('Before')
print(s1.name, s1.roll_no, s1.school_name)
print(s2.name, s2.roll_no, s2.school_name)

# Modify class variable using object reference
s1.school_name = 'PQR School'
print('After')
print(s1.name, s1.roll_no, s1.school_name)
print(s2.name, s2.roll_no, s2.school_name)

# A new instance variable is created for the s1 object, and this variable shadows the class variables. So always use the class name to modify the class variable.

# Class Variables In Inheritance

# We can use the parent class or child class name to change the value of a parent class’s class variable in the child class.

class Course:
    # class variable
    course = "Python"

class Student(Course):

    def __init__(self, name):
        self.name = name

    def show_student(self):
        # Accessing class variable of parent class
        print('Before')
        print("Student name:", self.name, "Course Name:", Student.course)
        # changing class variable value of base class
        print('Now')
        Student.course = "Machine Learning"
        print("Student name:", self.name, "Course Name:", Student.course)

# creating object of Student class
stud = Student("Emma")
stud.show_student()


# What if both child class and parent class has the same class variable name. In this case, the child class will not inherit the class variable of a base class. So it is recommended to create a separate class variable for child class instead of inheriting the base class variable.

# Example:

class Course:
    # class variable
    course = "Python"

class Student(Course):
    # class variable
    course = "SQL"

    def __init__(self, name):
        self.name = name

    def show_student(self):
        # Accessing class variable
        print('Before')
        print("Student name:", self.name, "Course Name:", Student.course)
        # changing class variable's value
        print('Now')
        Student.course = "Machine Learning"
        print("Student name:", self.name, "Course Name:", Student.course)

# creating object of Student class
stud = Student("Emma")
stud.show_student()

# parent class course name
print('Parent Class Course Name:', Course.course)




# Wrong Use of Class Variables

# In Python, we should properly use the class variable because all objects share the same copy. Thus, if one of the objects modifies the value of a class variable, then all objects start referring to the fresh copy.

class Player:
    # class variables
    club = 'Chelsea'
    sport = 'Football'

    def __init__(self, name):
        # Instance variable
        self.name = name

    def show(self):
        print("Player :", 'Name:', self.name, 'Club:', self.club, 'Sports:', self.sport)

p1 = Player('John')

# wrong use of class variable
p1.club = 'FC'
p1.show()

p2 = Player('Emma')
p2.sport = 'Tennis'
p2.show()

# actual class variable value
print('Club:', Player.club, 'Sport:', Player.sport)


# To avoid this, always modify the class variable value using the class name so that all objects gets the updated value. Like this

Player.club = 'FC'
Player.sport = 'Tennis'