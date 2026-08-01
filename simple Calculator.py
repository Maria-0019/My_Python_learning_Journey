a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))

def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  if (b==0):
    return "ERROR: cannot divide !"
    return a/b

print ("Simple Calculator")
print("1.Add=", add(a,b))
print("2.Subtract=", subtract(a,b))
print("3.Divide=", divide(a,b))
