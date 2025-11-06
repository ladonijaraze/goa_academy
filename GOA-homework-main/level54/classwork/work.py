#1)https://www.codewars.com/kata/5a03b3f6a1c9040084001765/train/python
def angle(n):
    if n > 2:
        return (n - 2) * 180
    else:
        return "n must be greater than 2"
#2)https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/python (edited)
def solution(arr):
    if arr is None or len(arr) == 0:
        return []
    
    return sorted(arr)
#3) https://www.codewars.com/kata/56b7f2f3f18876033f000307/train/python
def in_asc_order(arr):
    if len(arr) <= 1:
        return True
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    
    return True
