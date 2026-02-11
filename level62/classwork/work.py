#per =[
#    {"shop":"matemotors",},
#    {"shop":"matemotors",},
#    {"shop":"matemotors",},
#    {"shop":"matemotors",},
#    {"shop":"matemotors",}
#
#]
#for key in per:
#    print(key["shop"])

#შექმენით სია სადაც გვექნება 100 ელემენტის სია და გამოიტანეთ ყოველი მე -10 ციფრი list comporhension ით 

nums = list(range(1, 101))
tens= [nums[i] for i in range( len(nums), 10)]