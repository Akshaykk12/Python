
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + "." + last + "@email.com"

    @property                                                   #because of the property method we can call method as an attribute
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)
    
    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print("Delete Name")
        self.first = None
        self.last = None


emp_1 = Employee("John", "Smith")

emp_1.first = "Jim"

print(emp_1.first)
# print(emp_1.email())
print(emp_1.email)
print(emp_1.full_name())

del emp_1.full_name()