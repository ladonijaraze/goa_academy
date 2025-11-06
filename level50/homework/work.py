#2) https://www.codewars.com/kata/555086d53eac039a2a000083/train/python
def are_in_love(petals1, petals2):
    return (petals1 % 2 == 0 and petals2 % 2 != 0) or (petals1 % 2 != 0 and petals2 % 2 == 0)

#3) https://www.codewars.com/kata/56606694ec01347ce800001b/train/python
def can_form_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

#4) https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python
def longest(s1, s2):
    return ''.join(sorted(set(s1 + s2)))

#5) https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python
def invert(lst):
    return [-x for x in lst]

#6) https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for age, handicap in data]

#7) https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python
def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result


#8) https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python
def printer_error(s):
    errors = sum(1 for char in s if char not in 'abcdefghijklm')
    return f"{errors}/{len(s)}"

#9) https://www.codewars.com/kata/5556282156230d0e5e000089/train/python
def dna_to_rna(dna):
    return dna.replace('T', 'U')

#10) https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python
def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    if bmi_value <= 18.5:
        return "Underweight"
    elif bmi_value <= 25.0:
        return "Normal"
    elif bmi_value <= 30.0:
        return "Overweight"
    else:
        return "Obese"
