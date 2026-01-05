#1) https://www.codewars.com/kata/59cd0535328801336e000649/train/python
def interest(p, r, n):
    simple = round(p * (1 + r * n))
    compound = round(p * (1 + r)**n)
    return [simple, compound]


#2) https://www.codewars.com/kata/54e9554c92ad5650fe00022b/train/python
def to_currency(n):
    num_str = str(n)           
    result = ""                    
    count = 0                    
    

    for i in range(len(num_str) - 1, -1, -1):
        result = num_str[i] + result   
        count += 1                   
        if count % 3 == 0 and i != 0:
            result = "," + result
    
    return result

#3) https://www.codewars.com/kata/5497a3c181dd7291ce000700/train/python
def diagonal_sum(arrays):
    total = 0
    for i in range(len(arrays)):
        total += arrays[i][i] 
    return total

#4) https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python
def summation(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total
    
#5) https://www.codewars.com/kata/55c353487fe3cc80660001d4/train/python
def reorder_words(s):
    words = s.split()    
    upper_words = []       
    lower_words = []       

    for word in words:
        if word[0].isupper():       
            upper_words.append(word)
        elif word[0].islower():     
            lower_words.append(word)

    return ' '.join(upper_words + lower_words)
