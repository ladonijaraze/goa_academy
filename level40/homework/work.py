
#1) https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python
def remove_duplicate_words(s):
    words = s.split()
    seen = set()
    result = []
    
    for word in words:
        if word.lower() not in seen:
            seen.add(word.lower())
            result.append(word)
    
    return ' '.join(result)

#2) https://www.codewars.com/kata/57f609022f4d534f05000024/train/python
def stray(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

#3) https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/python
def solution(nums):
    return sum(nums)

#4) https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python
def solution(word):
    return [i for i, char in enumerate(word) if char.isupper()]

#5) https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
