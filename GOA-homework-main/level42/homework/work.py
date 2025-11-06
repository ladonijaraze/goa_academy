#https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python
def sum_mix(arr):
    return sum(int(i) for i in arr)

#https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python
def double_char(s):
    return ''.join([char * 2 for char in s])

#https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/train/python
def array_plus_array(arr1, arr2):
    return sum(arr1 + arr2)

#https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python
def reverse_words(s):
    return ' '.join(s.split()[::-1])

#https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python
def sum_str(a, b):

    a = int(a) if a else 0
    b = int(b) if b else 0
    return str(a + b)
