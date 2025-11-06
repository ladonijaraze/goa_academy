def arara_count(n):
    if n == 1:
        return "anane"
    
    result = 'adak ' * (n // 2)
    if n % 2 != 0:
        result += 'anane'
    
    return result

print(arara_count(3)) 
print(arara_count(8))  
#მას მინდა ედითი გავაკეთო მაგრამ იდეა არმაქვს, მომაწოდებთ იდეას?

def is_correct_mnemonic(solar_system, mnemonic):
    filtered_planets = [planet for planet in solar_system if planet != "Asteroid"]

    mnemonic_words = mnemonic.split()
    
    if len(filtered_planets) != len(mnemonic_words):
        return False

    for i in range(len(filtered_planets)):
        if filtered_planets[i][0] != mnemonic_words[i][0]:
            return False
    
    return True


print(is_correct_mnemonic(["Earth", "Jupiter", "Asteroid", "Asteroid", "Mercury", "Asteroid", "Saturn"], "Even Jaguars Make Spaghetti"))  
print(is_correct_mnemonic(["Asteroid", "Mars", "Uranus", "Asteroid"], "Water Melon"))  # False



#3
def max_score(testshi, new):
    total_score = 0
    
    for kitxvebi in testshi:
        if kitxvebi in new:
            total_score += testshi[kitxvebi] * 2
        else:
            total_score += testshi[kitxvebi]
    
    return total_score



