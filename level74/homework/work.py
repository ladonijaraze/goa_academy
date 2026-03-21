def apply_operation(numbers, operation):
    return [operation(x) for x in numbers]


def my_map(func, lst):
    result = []
    for item in lst:
        result.append(func(item))
    return result


def my_filter(func, lst):
    result = []
    for item in lst:
        if func(item):
            result.append(item)
    return result


def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier


def repeat(func, n):
    def wrapper(*args, **kwargs):
        for _ in range(n):
            func(*args, **kwargs)
    return wrapper


# მაგალითები
if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(apply_operation(nums, lambda x: x * 2))  # [2, 4, 6, 8]
    print(my_map(lambda x: x + 1, nums))           # [2, 3, 4, 5]
    print(my_filter(lambda x: x % 2 == 0, nums))   # [2, 4]

    double = make_multiplier(2)
    print(double(5))  # 10

    def say_hi():
        print("Hi")

    repeat_hi = repeat(say_hi, 3)
    repeat_hi()