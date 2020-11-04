# Source = https://www.youtube.com/watch?v=BJ-VvGyQxho&list=TLPQMzExMDIwMjDrzhKNjJ8DVg&index=2
print('Starting the03-class methods-static methods python file')


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

    '''class methods pass the class as an argument automatically'''
    @classmethod
    def change_rate_of_raise(cls, new_rate):
        cls.rate_of_raise = new_rate

    @classmethod
    def from_string(cls, student_string):
        first_name, last_name, pay = student_string.split('-')
        return cls(first_name, last_name, pay)

    '''static methods pass no argument automatically'''
    @staticmethod
    def is_school_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


jon = Student('Jon', 'Snow', 100)
arya = Student('Arya', 'Stark', 200)

# print('')
# print('When we are fetching the rate_of_raise which is the class variable via an instance => we get the value of the class variable')
# print('increment rate for jon = jon.rate_of_raise = ', jon.rate_of_raise)
# print('increment rate for arya = arya.rate_of_raise =', arya.rate_of_raise)
# print('increment rate for class Student = Student.rate_of_raise =', Student.rate_of_raise)
# print('')
# print('===================================================')
# print('')
#
# print('Changing increment rate for Student.rate_of_raise to 5%')
# Student.change_rate_of_raise(1.05)         # This method will automatically pass the class because it is a class method

'''Changing the class variable by invoking the class method via instance'''
# jon.change_rate_of_raise(1.05)                  # One can change the class variable via an instance, but it logically does not make sense
#
# # changing the class variable using the instance also does not include the variable in the dictionary values of the instance as the class variable changes for all
# print(jon.__dict__)
# print(arya.__dict__)

'''Using class methods as alternative constructors - means you can provide multiple ways to create objects'''

# input_student_string = 'John-Doe-1000'
#
# john = Student.from_string(input_student_string)
#
# print(john.first_name)
# print(john.last_name)
# print(john.pay)

# print('')
# print('Printing the rate_of_raise for the 2 instances and the class to clearly show how changing the class variable impacts all other instances')
# print('increment rate for jon = jon.rate_of_raise = ', jon.rate_of_raise)
# print('increment rate for arya = arya.rate_of_raise =', arya.rate_of_raise)
# print('increment rate for class Student = Student.rate_of_raise =', Student.rate_of_raise)

'''Using static methods from a class'''

import datetime

sunday_date = datetime.date(2020, 11, 1)                                        # this date is of a Sunday
print('is sunday_date a weekday? -', Student.is_school_day(sunday_date))       # Hence, it is not a weekday

monday_date = datetime.date(2020, 11, 2)                                        # this date is of a Monday
print('is monday_date a weekday? -', Student.is_school_day(monday_date))        # Hence, it is not a weekday
