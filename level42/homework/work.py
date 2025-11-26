#https://www.codewars.com/kata/53369039d7ab3ac506000467
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#https://www.codewars.com/kata/5513795bd3fafb56c200049e
def multiples(x, n):
    return [x * i for i in range(1, n + 1)]

#https://www.codewars.com/kata/59c1302ecb7fb48757000013
def type_validation(variable, type_name):
    type_mapping = {
        "int": int,
        "str": str,
        "float": float,
        "bool": bool,
        "list": list,
        "dict": dict,
        "tuple": tuple,
        "set": set
    }
    if type_name not in type_mapping:
        return False
    
    return isinstance(variable, type_mapping[type_name])

#https://www.codewars.com/kata/5641a03210e973055a00000d
def two_decimal_places(number):
    return round(number, 2)

#https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118
def remove_duplicates(arr):
    result = []
    for num in arr:
        if num not in result:
            result.append(num)
    return result
