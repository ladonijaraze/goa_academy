#1) https://www.codewars.com/kata/580751a40b5a777a200000a1/train/python
def vowelOne(s):
    vowels = 'aeiouAEIOU'  
    result = ''.join('1' if char in vowels else '0' for char in s)  
    return result

#2) https://www.codewars.com/kata/576400f2f716ca816d001614/train/python
import math

def reduce_fraction(fraction):
    numerator, denominator = fraction
    gcd = math.gcd(numerator, denominator)     
    reduced_numerator = numerator // gcd
    reduced_denominator = denominator // gcd
    
    return [reduced_numerator, reduced_denominator]

#3) https://www.codewars.com/kata/5738f5ea9545204cec000155/train/python
def count_letters_and_digits(s):
    count = 0
    for char in s:
        if char.isalnum():  #
            count += 1
    return count

#4) https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
def solution(string, ending):
    return string.endswith(ending)

#5) https://www.codewars.com/kata/5834315e06f227a6ac000099/train/python
def find_twins(arr):
    seen = set() 
    for num in arr:
        if num in seen:
            return num  
        seen.add(num)
    return None
