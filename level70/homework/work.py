# 1. მათემატიკური ოპერატორი
def apply_op(a, b, func):
    return func(a, b)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

print(apply_op(3, 4, add))
print(apply_op(3, 4, multiply))


# 2. სალმის გენერატორი
def make_greeter(greeting):
    def greeter(name):
        print(greeting, name)
    return greeter

say_hi = make_greeter("გამარჯობა")
say_hi("დავით")


# 3. მარტივი ფილტრი
def my_filter(lst, predicate):
    result = []
    for item in lst:
        if predicate(item):
            result.append(item)
    return result

def is_even(x):
    return x % 2 == 0

print(my_filter([1,2,3,4,5,6], is_even))

