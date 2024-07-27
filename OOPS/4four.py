
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

    @classmethod                                                                    #if variables in classmethod is changed then it changes for all the instances
    def set_raise_amt(cls, amount):                                                 #class method automatically pass the class (cls)as the first argument
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):                                                  #classmethod as an alternative  constructor
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)                                                #if we are not using cls class variable then there's no point in using classmethod
    
    @staticmethod
    def is_workday(day):                                                            #static method dont pass any arguments automatically
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        
        return True
    
emp_1= Employee("Akshay", "Kudalkar", 50000)                                         #instance of a class
emp_2= Employee("Durgest", "Kudalkar", 90000)                                        #instance of a class

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Amir-Khan-30000"
emp_str_3 = "Muzaffur-Seikh-90000"

# first, last, pay = emp_str_1.split("-")
# new_emp_1 = Employee(first, last, pay)

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
