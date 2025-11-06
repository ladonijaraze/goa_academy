#1
def validate_password(password):
   
    if len(password) < 8:
        return False

    
    has_upper = False
    has_lower = False
    has_digit = False

    for i in range(len(password)):
        if password[i].isupper():
            has_upper = True
        elif password[i].islower():
            has_lower = True
        elif password[i].isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        return True
    return False

#2
def is_isogram(string):
    string = string.lower()
    seen_chars = set()

    for char in string:
        if char in seen_chars:
            return False
        
        seen_chars.add(char)
    
 
    return True
#3
def filter_friends(names):
    filtered_names = []
    for name in names:
        if len(name) == 4:
            filtered_names.append(name)
    return filtered_names
#4
def validate_pin(pin):
    if len(pin) != 4 and len(pin) != 6:
        return False
    if not pin.isdigit():
        return False
    
    
    return True