#1
def my_split(text, delimiter):
    result = []
    word = ''
    
    for char in text:
        if char == delimiter:
            result.append(word)
            word = ''
        else:
            word += char
    
    if word:
        result.append(word)
    
    return result

text = "hello world this is python"
delimiter = ' '
print(my_split(text, delimiter))

#2
def my_join(word_list, delimiter):
    result = ''
    
    for i in range(len(word_list)):
        result += word_list[i]
        if i < len(word_list) - 1:
            result += delimiter
    
    return result

words = ["hello", "world", "this", "is", "python"]
delimiter = ' '
print(my_join(words, delimiter))

#3
def my_replace(text, old, new):
    result = ''
    i = 0
    while i < len(text):
        if text[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += text[i]
            i += 1
    return result

text = "hello world, hello again"
old = "hello"
new = "hi"
print(my_replace(text, old, new))

#4
def mini_calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

print(mini_calculator(10, 5, 'add'))        # 15
print(mini_calculator(10, 5, 'subtract'))   # 5
print(mini_calculator(10, 5, 'multiply'))   # 50
print(mini_calculator(10, 5, 'divide'))     # 2.0

#5
def get_words_and_join():
    words = []
    n = int(input("Enter the number of words: "))
    
    for _ in range(n):
        word = input("Enter a word: ")
        words.append(word)
    
    joined_words = ' '.join(words)
    print("Joined words:", joined_words)

get_words_and_join()
