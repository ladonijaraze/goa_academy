#1) https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python
def bool_to_word(b):
    return "Yes" if b else "No"

#2) https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python
def remove_char(s):
    return s[1:-1] if len(s) > 1 else ''

#3) https://www.codewars.com/kata/544675c6f971f7399a000e79/train/python
def string_to_number(s):
    try:
        return int(s) 
    except ValueError:
        try:
            return float(s)  
        except ValueError:
            return 

#4) https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python
def no_space(x):
    return x.replace(" ", "")

#5) https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/python
def sum_array(a):
    return sum(a)