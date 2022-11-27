
# for i in range(10,21):
#     f = open(r"C:\Users\RAHUL\Documents\OnePython\0.SelfStudy\{}.py".format(i) ,"w")
#     f.write("")

#################################################
#  
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON 
#################################################

# Constructor in Python


# A constructor is a special method used to create and initialize an object of a class. This method is defined in the class.

# The constructor is executed automatically at the time of object creation.
# The primary use of a constructor is to declare and initialize data member/ instance variables of a class. The constructor contains a collection of statements (i.e., instructions) that executes at the time of object creation to initialize the attributes of an object.


# In Python, Object creation is divided into two parts in Object Creation and Object initialization

# Internally, the __new__ is the method that creates the object
# And, using the __init__() method we can implement constructor to initialize the object.



# Syntax of a constructor

# def __init__(self):
#     # body of the constructor


# Example: Create a Constructor in Python

class Student:

    # constructor
    # initialize instance variable
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
        print('All variables initialized')

    # instance Method
    def show(self):
        print('Hello, my name is', self.name)


# create object using constructor
s1 = Student('Emma')
s1.show()


# In Python, we have the following three types of constructors.

        # Default Constructor
        # Non-parametrized constructor
        # Parameterized constructor
            # Constructor With Default Values

 # Default Constructor
class Employee:

    def display(self):
        print('Inside Display')

emp = Employee()
emp.display()


# Non-parametrized constructor
class Company:

    # no-argument constructor
    def __init__(self):
        self.name = "PYnative"
        self.address = "ABC Street"

    # a method for printing data members
    def show(self):
        print('Name:', self.name, 'Address:', self.address)

# creating object of the class
cmp = Company()

# calling the instance method using the object
cmp.show()



# Parameterized constructor
class Employee:
    # parameterized constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # display object
    def show(self):
        print(self.name, self.age, self.salary)

# creating object of the Employee class
emma = Employee('Emma', 23, 7500)
emma.show()

kelly = Employee('Kelly', 25, 8500)
kelly.show()

# Constructor With Default Values

class Student:
    # constructor with default values age and classroom
    def __init__(self, name, age=12, classroom=7):
        self.name = name
        self.age = age
        self.classroom = classroom

    # display Student
    def show(self):
        print(self.name, self.age, self.classroom)

# creating object of the Student class
emma = Student('Emma')
emma.show()

kelly = Student('Kelly', 13)
kelly.show()


# Self Keyword in Python

class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # self points to the current object
    def show(self):
        # access instance variable using self
        print(self.name, self.age)

# creating first object
emma = Student('Emma', 12)
emma.show()

# creating Second object
kelly = Student('Kelly', 13)
kelly.show()



# Constructor Overloading

# Python does not support constructor overloading. If we define multiple constructors then, the interpreter will considers only the last constructor and throws an error if the sequence of the arguments doesn’t match as per the last constructor. 


class Student:
    # one argument constructor
    def __init__(self, name):
        print("One arguments constructor")
        self.name = name

    # two argument constructor
    def __init__(self, name, age):
        print("Two arguments constructor")
        self.name = name
        self.age = age

# creating first object
emma = Student('Emma')

# creating Second object
kelly = Student('Kelly', 13)

# Constructor Chaining



# Constructor chaining is the process of calling one constructor from another constructor. Constructor chaining is useful when you want to invoke multiple constructors, one after another, by initializing only one instance.

# In Python, constructor chaining is convenient when we are dealing with inheritance. When an instance of a child class is initialized, the constructors of all the parent classes are first invoked and then, in the end, the constructor of the child class is invoked.

# Using the super() method we can invoke the parent class constructor from a child class



class Vehicle:
    # Constructor of Vehicle
    def __init__(self, engine):
        print('Inside Vehicle Constructor')
        self.engine = engine

class Car(Vehicle):
    # Constructor of Car
    def __init__(self, engine, max_speed):
        super().__init__(engine)
        print('Inside Car Constructor')
        self.max_speed = max_speed

class Electric_Car(Car):
    # Constructor of Electric Car
    def __init__(self, engine, max_speed, km_range):
        super().__init__(engine, max_speed)
        print('Inside Electric Car Constructor')
        self.km_range = km_range

# Object of electric car
ev = Electric_Car('1500cc', 240, 750)
print(f'Engine={ev.engine}, Max Speed={ev.max_speed}, Km range={ev.km_range}')



# Counting the Number of objects of a Class

# The constructor executes when we create the object of the class. For every object, the constructor is called only once. So for counting the number of objects of a class, we can add a counter in the constructor, which increments by one after each object creation.


class Employee:
    count = 0
    def __init__(self):
        Employee.count = Employee.count + 1


# creating objects
e1 = Employee()
e2 = Employee()
e2 = Employee()
print("The number of Employee:", Employee.count)


# Constructor Return Value
# In Python, the constructor does not return any value. Therefore, while declaring a constructor, we don’t have anything like return type. Instead, a constructor is implicitly called at the time of object instantiation. Thus, it has the sole purpose of initializing the instance variables.

class Test:

    def __init__(self, i):
        self.id = i
        return True

d = Test(10)

# OP>> TypeError: __init__() should return None, not 'bool'

