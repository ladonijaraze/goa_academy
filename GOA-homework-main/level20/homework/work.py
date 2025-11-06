words=["ლომი","ძაღლი","მგელი","ქათამი"]
vowels="აეიოუ"
def count_vowels(word):
    return sum(1 for letter in word if letter in vowels)
vowel_counts = [count_vowels(word) for word in words]
print(vowel_counts)

#2
დასაწყისი=0
დასასრული=200

სია=[cxeni for cxeni in range(დასაწყისი, დასასრული + 1) if cxeni % 5 == 0 or cxeni % 3 == 0]
print(სია)



#3
elements = ['a', 'b', '1', 'c', '2', 'd', '3']

result_string = ''.join(elements)

print(result_string)
#4
n = 4  


for i in range(n):
    
    print('' * i + '*' * (2 * (n - i) ))



#5
age = int(input("რამდენი წლის ხარ? "))

if age > 12:
    print("შენ არ ხარ 12 წლის")
else:
    print("welcome")

print("*"
    "*""*""*"
   "*""*""*""*")