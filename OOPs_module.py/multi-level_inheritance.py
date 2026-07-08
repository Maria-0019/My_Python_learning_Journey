# Base class
class A:
    def showA(self):
        print("This is class A")

# Derived from A
class B(A):
    def showB(self):
        print("This is class B")

# Derived from B
class C(B):
    def showC(self):
        print("This is class C")

# Main
obj = C()

obj.showA()  # from class A
obj.showB()  # from class B
obj.showC()  # from class C
