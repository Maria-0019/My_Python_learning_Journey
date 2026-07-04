num =int(input("Enter a number:"))

if num <=1:
  print(" not prime no")
else:
   is_prime_no = True
   for i in range (2, num):
      if num%i==0:
       is_prime_no= False
       break
   if is_prime_no:
      print("prime no.")
   else:
      print("not prime no.")
   
