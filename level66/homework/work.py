def sum_array(arr):
    return sum(arr)

def simple_multiplication(number) :
    if number %2:
    
        return number *9
    else:
        return number *8
    


def find_average(numbers):
    if len(numbers) == 0:
        return 0
    ave = 0 
    for num in numbers:
        ave += num
    return ave / len(numbers)
