
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

class Developer(Employee):                                                           #Developer is the subclass of the parent class Employee
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)   
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        
        if employees is None:
            self.employees = []
        else:
            self.employees = employees 

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp  in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())
    
emp_1= Developer("Akshay", "Kudalkar", 50000, "Python ")                                         #instance of a class
emp_2= Developer("Durgest", "Kudalkar", 90000, "Java")                                        #instance of a class

mng_1 = Manager("Sumit", "Dhawale", 80000, [emp_1])

print(isinstance(mng_1, Manager))
print(isinstance(mng_1, Employee))
print(isinstance(mng_1, Developer))

print(issubclass(Manager, Employee))


# mng_1.print_emp()
# mng_1.add_emp(emp_2)
# mng_1.remove_emp(emp_1)
# mng_1.print_emp()

# print(help(Developer))

# print(emp_1.email)
# print(emp_1.prog_lang)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
