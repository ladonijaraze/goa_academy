#1
names = ["დავით", "გიორგი", "თამარი", "დავით", "მარიამ", "დავით"]
name_to_count = "დავით"
count = names.count(name_to_count)
print(count)

#2
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

print("-------------")
#3
list_numbers = [1, 2, 3]
list = list_numbers * len(list_numbers)  
print(list)

#4
arr = ["Python", "html", "C++","js"]
arr.insert(1, "დავითი")  
print(arr)

#5
list = [1, 2, 3, 4, 2, 5, 2]
remove = 2

count = list.count(remove)  
list.remove(remove)  
print(list)