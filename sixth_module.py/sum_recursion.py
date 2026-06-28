# WAF to calculate the sum of first n natural number.

n= int(input("Enter a number:"))
 
def cal_sum(n):
    if(n==0):
        return 0
    else:
        return cal_sum(n-1)+n

print("Sum:", cal_sum(n))
