# WAP that print totl count of even and odd digits in a number.
N=int(input("Enter a number:"))
even=0
odd=0

while(N>0):
    rem=N%10

    if(rem%2==0):
        even+=1
    else:
        odd+=1
    
    N=N//10

print("Number of Even digits:",even)
print("Number of Odd digits:",odd)
