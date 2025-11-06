#1) https://www.codewars.com/kata/583710ccaa6717322c000105/train/python 
def multiply_number(n):
    if n % 2 == 0: 
        return n * 8
    else:  
        return n * 9

#2) https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python
def invert_numbers(nums):
    result = [] 
    for num in nums:
        result.append(-num)
    return result
#3) https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python
def fake_bin(x):
    result = ''
    for char in x:
        if int(char) < 5:
            result += '0'
        else:
            result += '1'
    return result
#4) https://www.codewars.com/kata/57e76bc428d6fbc2d500036d/train/python
def string_to_array(s):
    return s.split()
#5) https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python
def rps(player1, player2):
    if player1 == player2:
        return "Draw!"
    elif (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "rock" and player2 == "scissors"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"
#6) https://www.codewars.com/kata/5772da22b89313a4d50012f7/train/python
def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'
#7) https://www.codewars.com/kata/56f69d9f9400f508fb000ba7/train/python
def pre_count(n):
    return list(range(1, n + 1))
#8) https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python
def calculate_age(humanYears):
    if humanYears == 1:
        catYears = 15
    elif humanYears == 2:
        catYears = 24
    else:
        catYears = 24 + (humanYears - 2) * 4
    if humanYears == 1:
        dogYears = 15
    elif humanYears == 2:
        dogYears = 24
    else:
        dogYears = 24 + (humanYears - 2) * 5

    return [humanYears, catYears, dogYears]
#9) https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
def is_isogram(word):
    word = word.lower()  
    return len(set(word)) == len(word)  
#10) https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python
def is_isogram(word):
    word = word.lower()
    return len(set(word)) == len(word)  

