#1) https://www.codewars.com/kata/55b95c76e08bd5eef100001e/train/python
def count_arara(n):
    if n == 1:
        return "anane"
    elif n == 2:
        return "adak"
    else:
        pairs = n // 2  
        remainder = n % 2 
        result = "adak " * pairs  
        
        if remainder == 1:
            result += "anane"  
        
        return result.strip()
#2) https://www.codewars.com/kata/67d4554cd94fdfdab4239cfa/train/python
def is_planet_mnemonic_correct(planets, mnemonic):
    planet_letters = [planet[0] for planet in planets if planet != "Asteroid"]

    mnemonic_letters = [word[0] for word in mnemonic.split()]
    return planet_letters == mnemonic_letters

#3) https://www.codewars.com/kata/59656c69253c365e58000046/train/python
def max_possible_score(questions, new):
    total_score = 0
    for question, points in questions.items():
        if question in new:
            total_score += points * 2 
        else:
            total_score += points 
