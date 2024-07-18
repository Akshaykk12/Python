
class Employee:                                                                      #class

    raise_amount= 1.04                                                               #class variable
    num_of_emp = 0                                                                   #Lets create a class variable which will increment each time someone enters a new employee

    def __init__(self, first, last, pay):                                            #initialize or constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emp += 1

    def fullname(self):                                                              #method in which we pass the instance
        return "{} {}".format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
emp_1= Employee("Akshay", "Kudalkar", 50000)                                         #instance of a class
emp_2= Employee("Durgest", "Kudalkar", 90000)                                        #instance of a class

# print(emp_1.__dict__)                                                                #returns all the instance variables
# print(Employee.__dict__)                                                             #returns all class variables and methods

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.raise_amount = 1.05                                                             #we can change the attribute from outside class as well 

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)