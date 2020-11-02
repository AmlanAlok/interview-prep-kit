# Source = https://www.youtube.com/watch?v=BJ-VvGyQxho&list=TLPQMzExMDIwMjDrzhKNjJ8DVg&index=2
print('Starting the03-class methods-static methods python file')


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

    @classmethod
    def change_rate_of_raise(cls, new_rate):
        cls.rate_of_raise = new_rate


jon = Student('Jon', 'Snow', 100)
arya = Student('Arya', 'Stark', 200)


print('')
print('When we are fetching the rate_of_raise which is the class variable via an instance => we get the value of the class variable')
print('increment rate for jon = jon.rate_of_raise = ', jon.rate_of_raise)
print('increment rate for arya = arya.rate_of_raise =', arya.rate_of_raise)
print('increment rate for class Student = Student.rate_of_raise =', Student.rate_of_raise)
print('')
print('===================================================')
print('')

print('Changing increment rate for Student.rate_of_raise to 5%')
# Student.change_rate_of_raise(1.05)         # This method will automatically pass the class because it is a class method
jon.change_rate_of_raise(1.05)                  # One can change the class variable via an instance, but it logically does not make sense

# changing the class variable using the instance also does not include the variable in the dictionary values of the instance as the class variable changes for all
print(jon.__dict__)
print(arya.__dict__)

print('')
print('Printing the rate_of_raise for the 2 instances and the class to clearly show how changing the class variable impacts all other instances')
print('increment rate for jon = jon.rate_of_raise = ', jon.rate_of_raise)
print('increment rate for arya = arya.rate_of_raise =', arya.rate_of_raise)
print('increment rate for class Student = Student.rate_of_raise =', Student.rate_of_raise)

# print('When the class variable is changed for only a specific instance, then that variable gets added as a variable associated with the instance directly')
# print('Hence, you can see that for jon now there are 4 variables and arya still has 3 variables')
# print(jon.__dict__)
# print(arya.__dict__)
#
# print('')
# print('Printing the rate_of_raise for the 2 instances and the class to clearly show how changing the class variable impacts all other instances')
# print('increment rate for jon = jon.rate_of_raise = ', jon.rate_of_raise)
# print('increment rate for arya = arya.rate_of_raise =', arya.rate_of_raise)
# print('increment rate for class Student = Student.rate_of_raise =', Student.rate_of_raise)
#
# print('')
# print('===================================================')
# print('')
# print('Changing increment rate for Student.rate_of_raise to 1.04')
# Student.rate_of_raise = 1.04
#
#
# print('')
# print('===================================================')
# print('')
# print('Changing increment rate for jon to 1.1')
# jon.rate_of_raise = 1.10
# print('')
#
# print('When the class varibale is changed for only a specific instance, then that variable gets added as a variable associated with the instance directly')
# print('Hence, you can see that for jon now there are 4 variables and arya still has 3 variables')
# print(jon.__dict__)
# print(arya.__dict__)
#
# print('')
# print('Printing the rate_of_raise for the 2 instances and the class to clearly show how the same class variable now has different value for only once instance = jon')
# print('increment rate for jon = jon.rate_of_raise = ', jon.rate_of_raise)
# print('increment rate for arya = arya.rate_of_raise =', arya.rate_of_raise)
# print('increment rate for class Student = Student.rate_of_raise =', Student.rate_of_raise)
#
# print('')
# print('===================================================')
# print('')
# print('making jon.rate_of_raise = 1.04 again')
# jon.rate_of_raise = 1.04
#
# print('here you will notice that even though the value of jon.rate_of_raise has been changed back to 1.04, the instance will still have the variable in its dictionary')
# print(jon.__dict__)
# print(arya.__dict__)
