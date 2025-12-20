#1) https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
def reverse_words(text):
  word = ''
  rev_word = ''
  for i in range(0,len(text)):
      if(text[i] != ' '):
          word = word + text[i]
      else:
              rev_word = rev_word + word[::-1] + text[i]
              word = ''
  return(rev_word + word[::-1])
#2) https://www.codewars.com/kata/5949481f86420f59480000e7
def odd_or_even(arr):
    if not arr:
        arr = [0]
    total_sum = sum(arr)
    return "even" if total_sum % 2 == 0 else "odd"
#3) https://www.codewars.com/kata/542c0f198e077084c0000c2e
def divisors(n):
    count = 0
    i = 1
    
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        i += 1
        
    return count

#4) https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c
def sort_by_length(arr):
    result = arr[:] 

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if len(result[i]) > len(result[j]):
                temp = result[i]
                result[i] = result[j]
                result[j] = temp

    return result


#5) https://www.codewars.com/kata/59cfc000aeb2844d16000075
def capitalize(s):
    even = ""
    odd = ""
    
    for i, char in enumerate(s):
        if i % 2 == 0:
            even += char.upper()
            odd += char
        else:
            even += char
            odd += char.upper()
    
    return [even, odd]