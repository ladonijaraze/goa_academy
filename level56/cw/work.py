#1
def nugzar_chubinidze(sadgerdzelo, limit):
    if sadgerdzelo > limit:
        return "ნუგზარი აღარ დალიო მეტი!"
    else:
        return "მოდი ახლა მართლა, დამილოცნიე!"
#2
def yuri_gagarini():
    correct_pressure = 120
    correct_pulse = 80
    
    pressure = int(input("რა გაქვს გულის წნევა? "))
    pulse = int(input("რა გაქვს პულსი? "))
    
    if pressure == correct_pressure and pulse == correct_pulse:
        return True
    else:
        return False
#3
def captainjack(gold_coin):
    ships = [150, 200, 250, 300, 350]

    if gold_coin == 0:
        return "ეკიპაჟი აჯანყდება!"

    for ship in ships:
        if gold_coin >= ship:
            return f"კაპიტანმა აირჩია გემი {ship} ოქროს მონეტიანი!"

    return "ეკიპაჟი აჯანყდება!"
#4
def unique_apples(apple_list):
    return list(set(apple_list))

apple_list = ["პანტა", "პანტა", "გორული"]
print(unique_apples(apple_list))
#5)https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python
def solve(s):
    uppercase_count = sum(1 for c in s if c.isupper())
    lowercase_count = len(s) - uppercase_count  
    
    if uppercase_count > lowercase_count:
        return s.upper()
    else:
        return s.lower()
