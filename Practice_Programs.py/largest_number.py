# WAP that determines the maximum digit
N= int(input("Enter a number:"))

large=0

while(N>0):
    digit= N%10

    if(digit>large):
        large=digit

    N=N//10

print("Largest digit:",large)
