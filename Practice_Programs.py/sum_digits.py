# WAP that computes and print the sum of digits.
N= int(input("Enter a Number:"))
sum=0

while(N>0):
    rem=N%10
    sum=sum+rem
    N=N//10

print("sum of digits:", sum)
