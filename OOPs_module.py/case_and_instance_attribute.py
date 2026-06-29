class Student:
    college_name= "ABC college"   # class attr

    def __init__(self, name):
        self.name= name           # object attr
        
s1= Student("maria")
print(s1.name)

s2= Student("sadia")
print(s2.name)

s3= Student("sumna")
print(s3.name)

print(Student.college_name)
