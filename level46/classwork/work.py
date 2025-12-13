def square_digits(num):
    re = ""
    for x in str(num):
        re += str(int(x)**2)
    return int(re)
