def is_isogram(string):
    string = string.lower()
    for i in range(len(string)):
        if string[i] in string[:i]:
            return False
    return True
#ff