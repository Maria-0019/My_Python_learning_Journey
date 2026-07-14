# WAP that prints all the factors (in ascending order)
N=int(input("Enter a number:"))

for i in range (1,N+1):
    if(N%i==0):
        print("factors:", i)
