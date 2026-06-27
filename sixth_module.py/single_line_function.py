# WAF to print the elements of  alist in a single line (list in the parameter)

animals=["tiger", "deer", "fox", "jackle"]

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(animals)
