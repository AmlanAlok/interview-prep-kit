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


class Manager(Student):

    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        print('--------------------')
        for emp in self.employees:
            emp.full_name()
        print('--------------------')


jon = Developer('Jon', 'Snow', 100, 'Python')
arya = Developer('Arya', 'Stark', 200, 'Java')

print(jon.__dict__)
print(arya.__dict__)

'''------------- Learning 2: Using Manager subclass to maintain code -----------------'''

mgr_1 = Manager('Bran', 'Stark', 300, [jon])

# print(mgr_1.__dict__)
mgr_1.print_emps()              # showing employees added via constructor

mgr_1.add_emp(arya)             # adding new employee

mgr_1.print_emps()              # displaying both the employees

mgr_1.remove_emp(jon)           # removing employee = jon

mgr_1.print_emps()              # displaying employees after removing employee = jon

'''------------- Learning 1: Referencing class variables from parent class and subclass -----------------'''
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


'''Use of isinstance function'''
print('')
print('Use of isinstance function')
print('is mgr_1 instance of Manager class?', isinstance(mgr_1, Manager))
print('is mgr_1 instance of Student class?', isinstance(mgr_1, Student))
print('is mgr_1 instance of Developer class?', isinstance(mgr_1, Developer))

print('is jon instance of Developer class?', isinstance(jon, Developer))
print('is jon instance of Student class?', isinstance(jon, Student))
print('is jon instance of Manager class?', isinstance(jon, Manager))

'''Use of issubclass function'''
print('')
print('Use of issubclass function')
print('is Manager subclass of Student class?', issubclass(Manager, Student))
print('is Developer subclass of Student class?', issubclass(Developer, Student))
print('is Manager subclass of Developer class?', issubclass(Manager, Developer))
print('is Developer subclass of Manager class?', issubclass(Developer, Manager))
