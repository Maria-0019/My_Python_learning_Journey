# define a circle class to create a circle with radius r using the constructor.

class Circle:
    def __init__(self, radius):
        self.radius= radius

# define an area() method of the class which calculate the area of the circle.

    def area(self):
        return (22*self.radius**2)/7

 # define perimeter() method of the class which allow you to calculate the perimeter of the circle.
    
    def perimeter(self):
        return (2*22*self.radius)/7
    

c1=Circle(21)
print(c1.radius)
print(c1.area())
print(c1.perimeter())
