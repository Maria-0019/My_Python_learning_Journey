class Student:
   # Default constructors 
    def __init__(self):
        pass

    
   # Parameterized constructor
    def __init__(self, fullname, marks):
        self.name= fullname
        self.marks= marks
        print("adding new information")
        
s1= Student("mohan", 95)
print(s1.name, s1.marks)

s2= Student("sohan", 98)
print(s2.name, s2.marks)
