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


