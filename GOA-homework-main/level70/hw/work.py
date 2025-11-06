#1) https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python
def double_char(s):
    return ''.join([char * 2 for char in s])

#2) https://www.codewars.com/kata/563e320cee5dddcf77000158/train/python
def get_average(marks):
    return int(sum(marks) / len(marks))


#3) https://www.codewars.com/kata/515e188a311df01cba000003/train/python
def get_planet_name(id):
    planets = [
        "Mercury", "Venus", "Earth", "Mars", 
        "Jupiter", "Saturn", "Uranus", "Neptune"
    ]
    return planets[id - 1]

#4) https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))

#5) https://www.codewars.com/kata/5899642f6e1b25935d000161/train/python
def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))
