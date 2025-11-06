#1
#შექმენით ფუნქცია სახელად manual_difference, რომელიც არგუმენტად მიიღებს ორ sets, ფუნქციამ უნდა იმუშაოს იგივენაირად, როგორც ჩაშენებული ფუნქცია .difference
def manual_difference(set1, set2):
    result = set()  
    for element in set1:
        if element not in set2:  
            result.add(element)  
    return result
#მას ამას წინ უნდა დავუწეროთ set1 და set2
#2
#1)შექმენით 2 dict სხვადასხვა მოსწავლის ინფრომაციით, ინფორმაციასში უნდა შედიოდეს: ასაკი, საშუალო ქულა, სახელი და გვარი. შემდეგ გამოიტანეთ ორივე მოსწავლის ყველა ინფორმაცია
student_1 = {
    "სახელი": "ნიკა",
    "გვარი": "მამალაძე",
    "ასაკი": 17,
    "საშუალო ქულა": 8.5
}


student_2 = {
    "სახელი": "მარიამ",
    "გვარი": "გოგოლაძე",
    "ასაკი": 16,
    "საშუალო ქულა": 9.2
}


print("მოსწავლის 1 ინფორმაცია:")
for key, value in student_1.items():
    print(key + ": " + str(value))

print("\nმოსწავლის 2 ინფორმაცია:")
for key, value in student_2.items():
    print(key + ": " + str(value))
