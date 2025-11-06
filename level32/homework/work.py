#https://www.codewars.com/kata/57e76bc428d6fbc2d500036d
def string_to_array(s):
    return s.split()

print(string_to_array("Robin Singh"))
print(string_to_array("I love arrays they are my favorite"))
#)https://www.codewars.com/kata/544675c6f971f7399a000e79
def string_to_number(s):
    return int(s)

#https://www.codewars.com/kata/544675c6f971f7399a000e79 ეს იგივეა რაც მეორე🙂🙂
def string_to_number(s):
    return int(s)

#https://www.codewars.com/kata/57eae65a4321032ce000002d
def fake_bin(x):
    result = ""
    for digit in x:
        if int(digit) < 5:
            result += '0'
        else:
            result += '1'
    return result
#https://www.codewars.com/kata/554b4ac871d6813a03000035
def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))
    return f"{max(num_list)} {min(num_list)}"