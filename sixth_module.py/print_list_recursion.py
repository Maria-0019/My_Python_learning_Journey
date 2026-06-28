# WAF to print all the elements in a list.  Hint: use list and index as a parameters.

list= ["a", "b", "c", "d", "e"]

def print_list(list, idx=0):
    if (idx==len(list)):
       return 
    print(list[idx])
    print_list(list,idx+1)

print_list(list)
