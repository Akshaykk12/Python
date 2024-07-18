
class Employee:                                                                      #class
    
    def __init__(self, first, last, pay):                                            #initialize or constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):                                                              #method in which we pass the instance
        return "{} {}".format(self.first,self.last)

emp_1= Employee("Akshay", "Kudalkar", 50000)                                         #instance of a class
emp_2= Employee("Durgest", "Kudalkar", 90000)                                        #instance of a class

# print(emp_1)
# print(emp_2)

# emp_1.first = "Akshay"
# emp_1.last = "Kudalkar"
# emp_1.email = "akshaykudalkar.12@gmail.com"
# emp_1.pay = 50000

# emp_2.first = "Durgesh"
# emp_2.last = "Kudalkar"
# emp_2.email = "dkudalkarsr2j@gmail.com"
# emp_2.pay = 90000

print(emp_1.email)                                                                  #attribute
print(emp_2.email)                                                                  #attribute
print(emp_1.fullname())                                                             #method