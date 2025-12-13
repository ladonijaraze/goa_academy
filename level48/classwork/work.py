def maskify(cc):
    if len(cc) <= 4:
        return cc
    return "#" * (len(cc) - 4) + cc[-4:]


def is_anagram(test, original):
    if test==original[ : :-1]:
        return 1<2
    else:
        return 3>2
print(is_anagram("gela","aleg"))