#https://www.codewars.com/kata/5715eaedb436cf5606000381
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
#https://www.codewars.com/kata/515e271a311df0350d00000f
def square_sum(numbers):
    return sum(x**2 for x in numbers)
#https://www.codewars.com/kata/53dc54212259ed3d4f00071c
def sum_array(a):
    return sum(a)
#https://www.codewars.com/kata/57a2013acf1fa5bfc4000921
def find_average(numbers):
    if len(numbers) == 0:  
        return 0  
    return sum(numbers) / len(numbers)
#https://www.codewars.com/kata/576bb71bbbcf0951d5000044
def count_positives_sum_negatives(arr):
    count_positives = sum(1 for x in arr if x > 0)
    
    
    sum_negatives = sum(x for x in arr if x < 0)
    
    
    return [count_positives, sum_negatives]
