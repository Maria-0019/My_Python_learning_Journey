# WAP that counts the totol number of digits present in the number.
a=int(input("Enter a number:"))
count=0

while(a>0):
    a=a//10
    count+=1
    
print("totol digits:", count)


