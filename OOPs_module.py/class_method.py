class Person:
    name= "anonymous"
    
    @classmethod
    def changeName(cls, name):
        cls.name= name

p1= Person()      
p1.changeName("Maria")
print(p1.name)
