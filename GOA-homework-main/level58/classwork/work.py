def longest_word(s):
    longest = ""
    for word in s.split():
        if len(word) >= len(longest):
            longest = word
    return longest


print(longest_word("red white blue"))  

print(longest_word("red blue gold"))