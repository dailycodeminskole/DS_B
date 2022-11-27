#################################################
#  
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON 
# 👉 Python Static Method
#################################################   

# Python Static Method

# Static methods: A static method is a general utility method that performs a task in isolation. Inside this method, we don’t use instance or class variable because this static method doesn’t take any parameters like self and cls.

class Employee:
    @staticmethod
    def sample(x):
        print('Inside static method', x)

# call static method
Employee.sample(10)

# can be called using object
emp = Employee()
emp.sample(10)


# Example: Create Static Method Using @staticmethod Decorator

class Employee(object):

    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.gather_requirement(self.project_name)
        for task in requirement:
            print('Completed', task)

emp = Employee('Kelly', 12000, 'ABC Project')
emp.work()


# The staticmethod() function

class Employee:
    def sample(x):
        print('Inside static method', x)

# convert to static method
Employee.sample = staticmethod(Employee.sample)
# call static method
Employee.sample(10)


# Call Static Method from Another Method

class Test :
    @staticmethod
    def static_method_1():
        print('static method 1')

    @staticmethod
    def static_method_2() :
        Test.static_method_1()

    @classmethod
    def class_method_1(cls) :
        cls.static_method_2()

# call class method
Test.class_method_1()