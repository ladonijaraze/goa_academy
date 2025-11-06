#1) https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
def solution(string, ending):
    return string.endswith(ending)

#2) https://www.codewars.com/kata/57f7b8271e3d9283300000b4/train/python
def even_or_odd(string):
    even_sum = 0
    odd_sum = 0

    for char in string:
        digit = int(char)

        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    if even_sum > odd_sum:
        return "Even is greater than Odd"
    elif odd_sum > even_sum:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"

#3) https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c/train/python
def even_numbers(arr, num):
    even_numbers = [x for x in arr if x % 2 == 0]

    return even_numbers[-num:]

#4) https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python
def vowel_indices(word):
    vowels = 'aeiouAEIOU' 
    result = []

    for i, char in enumerate(word):
        if char in vowels:
            result.append(i + 1) 
    return result

#5) https://www.codewars.com/kata/55caef80d691f65cb6000040/train/python 
def geometric_sequence_elements(a, r, n):
    sequence = []

    for i in range(n):
        sequence.append(a * r**i)

    return ', '.join(map(str, sequence))
