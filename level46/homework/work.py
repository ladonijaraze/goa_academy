#1
#https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
def high_and_low(numbers):
    
    num_list = [int(num) for num in numbers.split()]
    highest = max(num_list)
    lowest = min(num_list)

    return f"{highest} {lowest}"
#2
#https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()
#3
#https://www.codewars.com/kata/5949481f86420f59480000e7/train/python
def odd_or_even(arr):
    if not arr:
        arr = [0]
    total_sum = sum(arr)
    return "even" if total_sum % 2 == 0 else "odd"
#4
#https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/python
def solution(arr):
    if arr is None or len(arr) == 0:
        return []
    return sorted(arr)
#5
#https://www.codewars.com/kata/535474308bb336c9980006f2/train/python
def greet(name):
    return "Hello " + name.capitalize() + "!"
#commmmmm