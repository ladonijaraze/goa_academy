#1)https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python
def no_space(x):
    return x.replace(" ","")

#2)https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
def count_sheeps(sheep):
    if not sheep:
        return 0
    count = 0
    for s in sheep:
        if s is True:
            count += 1
    return count
#3)https://www.codewars.com/kata/523b4ff7adca849afe000035/train/python
def greet():
    return "hello world!"
#4)https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python
def summation(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total

#5)https://www.codewars.com/kata/544675c6f971f7399a000e79/train/python
def string_to_number(s):
    return int(s)