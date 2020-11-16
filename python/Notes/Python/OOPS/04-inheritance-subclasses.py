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
        self.pay = int(self.pay * self.rate_of_raise)


class Developer(Student):
    rate_of_raise = 1.10

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)            # this will pass the 3 var to the init method of the Student class
        # Student.__init__(self, first_name, last_name, pay)    # this approach also works here but once you start to enter multiple inheritance using super() is necessary
        self.prog_lang = prog_lang


jon = Developer('Jon', 'Snow', 100, 'Python')
arya = Developer('Arya', 'Stark', 200, 'Java')

print(jon.__dict__)
print(arya.__dict__)

# '''------------- Learning 1: Referencing class variables from parent class and subclass -----------------'''
# print(jon.pay)
# '''This func will refer the class variable value from the subclass if that var is available or else, it will refer the value of the variable from the parent class.
# This way if you want a certain group to have a different value for a class var, you can do it.'''
# jon.get_new_pay()
# print(jon.pay)

# '''This help command helps you see all the information regarding the class you are referring to'''
# print(help(Developer))

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

# '''This help command helps you see all the information regarding the class you are referring to'''
# print(help(Student))
