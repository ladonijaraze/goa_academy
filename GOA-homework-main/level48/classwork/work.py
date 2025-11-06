#1
def XO(string):
    x_count = 0
    o_count = 0
    for char in string.lower():
        if char == 'x':
            x_count += 1
        elif char == 'o':
            o_count += 1
    return x_count == o_count
#2
def find_short(s):
    words = s.split()
    shortest_length = float('inf')

    for word in words:
        word_length = len(word)
        if word_length < shortest_length:
            shortest_length = word_length 

    return shortest_length
#3
def solution(string, ending):
    if len(ending) > len(string):
        return False
    ending_part = string[-len(ending):]
    if ending_part == ending:
        return True
    else:
        return False
#4
def accum(s):
    result = []
    for i, char in enumerate(s):
        result.append(char.upper() + char.lower() * i)
    return '-'.join(result)


