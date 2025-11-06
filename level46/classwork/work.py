#1
def filter_list(lst):
    result = [] 
    for item in lst:  
        if type(item) == int:  
            result.append(item)  
    return result
#2
def remove_vowels(zebra):
    vowels = "aeiouAEIOU"  
    result = ""
    for lomi in zebra:
        if lomi not in vowels:
            result 
    return result
#3
def descending_order(num):
    num_str = str(num) 
    num_list = [] 
    for digit in num_str:
        num_list.append(digit)
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] < num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    return int(''.join(num_list))
