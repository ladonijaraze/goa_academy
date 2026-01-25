#1) https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/javascript
def filter_list(l):
    result = []

    for item in l:
        if isinstance(item, int):
            result.append(item)
    return result

#2) https://www.codewars.com/kata/554b4ac871d6813a03000035/train/javascript
def high_and_low(numbers):
    
    num_list = [int(num) for num in numbers.split()]
    highest = max(num_list)
    lowest = min(num_list)
    
    return f"{highest} {lowest}"
#3) https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/javascript
def get_count(s):
    vovls = 0
    for let in s:
        if let in "aeiou":
            vovls=vovls+ 1
    return vovls
#4) https://www.codewars.com/kata/55908aad6620c066bc00002a/train/javascript
def xo(s):
    x = 0
    o = 0

    for char in s.lower():
        if char == 'x':
            x = x + 1
        elif char == 'o':
            o = o + 1

    return x == o