# Parent Class 1
class Fruit:
    def taste(self):
        print("Fruits are sweet ")

# Parent class 2
class Color:
    def color(self):
        print("Fruits have colors ")

# Child class (inherits both)
class Apple(Fruit, Color):
    def info(self):
        print("Apple is healthy")
