num= int(input("Enter a number:"))

original_sum=sum
sum=0

while num>0:
  digit=num % 10
  sum=sum + digit**3
  num num//10

if sum== original_sum:
  print(" Armstrong number")
else:
  print("not armstrong number")
