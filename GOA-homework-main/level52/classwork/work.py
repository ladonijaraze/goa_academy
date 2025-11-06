#1
def find_next_square(n):
    mr_davit = int(n ** 0.5) 
    if mr_davit * mr_davit == n:
        return (mr_davit + 1) ** 2
    else:
        return -1
#2
def min_max(list):
    return [min(list), max(list)]
#3
def series_sum(n):
    if n == 0:
        return "0.00"
    
    total_sum = 0
    for k in range(n):
        total_sum += 1 / (3 * k + 1)