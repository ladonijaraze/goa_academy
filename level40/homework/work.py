#https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
def digitize(n):
    return [int(d) for d in str(n)][::-1]

#https://www.codewars.com/kata/555086d53eac039a2a000083/train/python
def are_in_love(petals1, petals2):
    return (petals1 % 2 == 0 and petals2 % 2 != 0) or (petals1 % 2 != 0 and petals2 % 2 == 0)

#https://www.codewars.com/kata/57f781872e3d8ca2a000007e/train/python
def maps(arr):
    return [x * 2 for x in arr]

#https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7/train/python
def make_upper_case(s):
    return s.upper()

#https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python
def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    return n * m
