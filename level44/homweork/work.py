#3
def binary_array_to_number(arr):

    return int(''.join(map(str, arr)), 2)
#4
def min_max(arr):
    return [min(arr), max(arr)]
#5
def divisors(n):
    if n <= 1:
        raise ValueError("n must be greater than 1")
    
    divs = []
    
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            divs.append(i)
            if i != n // i:  
                divs.append(n // i)
    
    divs.sort()
    
    if divs:
        return divs
    else:
        return f"{n} is prime"

