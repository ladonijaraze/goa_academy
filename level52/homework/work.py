#1) https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/python
def multi_table(number):
    result = []
    for i in range(1, 11):
        result.append(str(i) + " * " + str(number) + " = " + str(i * number))
    return "\n".join(result)
#2) https://www.codewars.com/kata/56e2f59fb2ed128081001328/train/python
def array_to_string(arr):
    str_elements = []
    for element in arr:
        str_elements.append(str(element))
    return ",".join(str_elements)

#3) https://www.codewars.com/kata/57e1e61ba396b3727c000251/train/python
import re

def string_clean(s):
    s = re.sub(r'[^a-zA-Z0-9\s]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()

    return s

#4) https://www.codewars.com/kata/5b39e91ee7a2c103300018b3/train/python
def remove_consecutive_duplicates(s):
    words = s.split()
    result = []
    for word in words:
        if not result or word != result[-1]:
            result.append(word)
    return ' '.join(result)

#5) https://www.codewars.com/kata/56d19b2ac05aed1a20000430/train/python
def find_difference(arr):

    largest = max(arr)
    smallest = min(arr)

    return largest - smallest

