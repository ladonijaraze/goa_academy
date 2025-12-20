#1) https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/python
def capitalize(s):
    even = ""
    odd = ""
    
    for i, char in enumerate(s):
        if i % 2 == 0:
            even += char.upper()
            odd += char
        else:
            even += char
            odd += char.upper()
    
    return [even, odd]

#2) https://www.codewars.com/kata/5300901726d12b80e8000498/train/python
def fizzbuzz(n):
    result = []
    
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)  
    return result

#3) https://www.codewars.com/kata/535474308bb336c9980006f2/train/python
def greet(name):
    return "Hello " + name.capitalize() + "!"
#4) https://www.codewars.com/kata/5966eeb31b229e44eb00007a/train/python
def vaporcode(s):
    return "  ".join(s.replace(" ", "").upper())
#5) https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5/train/python
def reverse_number(n):
    sign = -1 if n < 0 else 1
    reversed_digits = int(str(abs(n))[::-1])
    return sign * reversed_digits
