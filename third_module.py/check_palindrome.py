# WAP to check if a list contains a palindrome of elements.

list = ["M", "A", "A", "M"]
copy_list = list.copy()
copy_list.reverse()

if (copy_list ==list):
    print("palindrome")
else:
    print("NOT palindrome")
