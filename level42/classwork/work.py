def basic_op(operation, value1, value2):
    if operation == '+':
        return value1 + value2
    elif operation == '-':
        return value1 - value2
    elif operation == '*':
        return value1 * value2
    elif operation == '/':
        return value1 / value2


def area_or_perimeter(length, width):
    if length == width:
        return length * width
    else:                 
        return 2 * (length + width)
