print('Starting the classes python file')


class Student:

    """self is the instance of the class that is getting passed automatically"""
    """__init__ is the equivalent of a constructor"""
    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        print('Full Name = {} {}'.format(self.first_name, self.last_name))


john = Student('John', 'Oliver')
naruto = Student('Naruto', 'Uzumaki')

print(john.first_name)
print(naruto.first_name)

"""This is one way to make function calls for an instance"""
john.full_name()            # this works as the function is been invoked via an instance, so python automatically passed the instance as an argument to self
naruto.full_name()          # this works as the function is been invoked via an instance, so python automatically passed the instance as an argument to self

"""This creates an error as python passes one argument automatically and you are passing one argument manually. But, the function has room for only one argument"""
# john.full_name(john)        # TypeError: full_name() takes 1 positional argument but 2 were given

"""
This is the second way to make function calls for an instance
Here, we refer the function full_name via the class name and hence, python does not know which instance to refer.
So, python cannot automatically pass the instance for the self argument in the function. Therefore, you will have
to do it manually.
"""
Student.full_name(john)                 # this works as we are manually passing the instance argument as self
Student.full_name(naruto)               # this works as we are manually passing the instance argument as self

"""
This creates an error as python does not know which instance to refer so it did not automatically pass an argument for self and the user has not passed an instance 
manually for the self argument. So, there is an expectation for 1 argument but nothing is been passed.
"""
# Student.full_name()                 # TypeError: full_name() missing 1 required positional argument: 'self'
