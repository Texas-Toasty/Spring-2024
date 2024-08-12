class Employee:
    def __init__(self, name, id, dept, title):
        self.name = name
        self.id = id
        self.dept = dept
        self.title = title


employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
print(employee1.name, employee1.id, employee1.dept, employee1.title)
print(employee2.name, employee2.id, employee2.dept, employee2.title)
print(employee3.name, employee3.id, employee3.dept, employee3.title)
