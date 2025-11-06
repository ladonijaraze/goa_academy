
double = lambda x: x * 2
print(double(5))  

string_length = lambda s: len(s)
print(string_length("გამარჯობა"))  


is_odd = lambda x: x % 2 != 0
print(is_odd(3))  
print(is_odd(4))   


square = lambda x: x ** 2
print(square(6))  

def even_squares(numbers):
    return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

nums = [1, 2, 3, 4, 5, 6]
print(even_squares(nums))  
