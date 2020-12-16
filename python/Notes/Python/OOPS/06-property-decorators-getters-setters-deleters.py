# Source = https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6
print('Starting the 06-property-decorators-getters-setters-deleters python file')


class Student:

    rate_of_raise = 1.04

    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name
        # self.email = self.first_name + '.' + self.last_name + '@email.com'

    @property           # this decorator allows you to use a function name as a property/attribute
    def email(self):
        return '{}.{}@email.com'.format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return 'Full Name = {} {}'.format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

    @full_name.deleter
    def full_name(self):
        print('Deleting full name')
        self.first_name = None
        self.last_name = None


jon = Student('Jon', 'Snow')

jon.first_name = 'Jim'

print(jon.__dict__)
print(jon.email)            # this reference is not to a func, but to a property due to the property decorator
print(jon.full_name)        # this reference is not to a func, but to a property due to the property decorator

print('')
print('Changing the Student objects full name')
jon.full_name = 'Polo Peters'
print('Displaying full name after change')
print(jon.full_name)

print('')
del jon.full_name
print('Displaying full name after deletion')
print(jon.full_name)




