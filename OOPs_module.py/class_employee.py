class Employee:
    def __init__(self, role, department, salary):
        self.role= role
        self.department= department
        self.salary=salary
    
    def showDetails(self):
        print("role=", self.role)
        print("department=", self.department)
        print("salary=", self.salary)


emp1= Employee( "accountant", "Finance", "100000")
emp1.showDetails()
