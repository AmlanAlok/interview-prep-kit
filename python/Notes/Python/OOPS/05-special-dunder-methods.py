# Source = https://www.youtube.com/watch?v=3ohzBxoFHAY&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=5
print('Starting the 05-special-dunder-methods python file')


class Student:

    rate_of_raise = 1.04

    def __init__(self, first_name, last_name, pay):

        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    def full_name(self):
        print('Full Name = {} {}'.format(self.first_name, self.last_name))

    def get_new_pay(self):

        print('New Pay = {}'.format(self.pay * self.rate_of_raise))

    def __repr__(self):
        return "Student('{}', '{}', {})".format(self.first_name, self.last_name, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.first_name + ' ' + self.last_name, self.pay)

    '''Returns the sum of the salaries of the two employees'''
    def __add__(self, other):
        return self.pay + other.pay

    '''Returns the length of first name + last name'''
    def __len__(self):
        return len(self.first_name + ' ' + self.last_name)


jon = Student('Jon', 'Snow', 100)
arya = Student('Arya', 'Stark', 200)

'''This will now first reference the str dunder method. If absent, then reference the repr dunder method'''
print(jon)


'''Assessing the repr and str dunder method independently'''
print('')
print('Assessing the repr and str dunder method independently')
print(repr(jon))
print(str(jon))

print('')
print(jon.__repr__())
print(jon.__str__())


'''Python print func behaves differently to the add operation depending on the input'''
print('')
print(1+2)
print('a'+'b')

'''The actual function being invoked under the hood is as below (dunder add)'''
print('')
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

'''creating custom add dunder method'''
print('')
print('Combined pay of jon and arya')
print(jon + arya)                   # If no custom add dunder method is implemented, TypeError: unsupported operand type(s) for +: 'Student' and 'Student'

'''creating custom len dunder method'''
print('')
print('Length of first name + last name')
print(len(jon))                     # If no custom len dunder method is implemented, TypeError: object of type 'Student' has no len()
