# Source - https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4
print('Starting the 04-inheritance-subclasses.py script')


class Student:
    rate_of_raise = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    '''regular methods pass the instance as an argument automatically'''

    def full_name(self):
        print('Full Name = {} {}'.format(self.first_name, self.last_name))

    def get_new_pay(self):
        print('New Pay = {}'.format(self.pay * self.rate_of_raise))


class Developer(Student):
    pass


jon = Developer('Jon', 'Snow', 100)
arya = Developer('Arya', 'Stark', 200)

print(jon.__dict__)
print(arya.__dict__)

'''This help command helps you see all the information regarding the class you are referring to'''
print(help(Developer))

# Help on class Developer in module __main__:
#
# class Developer(Student)
#  |  Developer(first_name, last_name, pay)
#  |
#  |  Method resolution order:
#  |      Developer
#  |      Student
#  |      builtins.object
#  |
#  |  Methods inherited from Student:
#  |
#  |  __init__(self, first_name, last_name, pay)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  full_name(self)
#  |
#  |  get_new_pay(self)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors inherited from Student:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes inherited from Student:
#  |
#  |  rate_of_raise = 1.04
#
# None

'''This help command helps you see all the information regarding the class you are referring to'''
print(help(Student))