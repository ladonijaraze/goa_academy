# set_functions.py

print("Set functions:")

my_set = {1, 2, 3, 4, 5}

my_set.add(6)
print("After add:", my_set)

my_set.remove(3)
print("After remove:", my_set)

my_set.discard(4)
print("After discard:", my_set)

my_set.clear()
print("After clear:", my_set)

my_set = {1, 2, 3, 4, 5}
removed_element = my_set.pop()
print("After pop:", my_set, "Removed element:", removed_element)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of sets:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

difference_set = set1.difference(set2)
print("Difference of sets:", difference_set)

sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric difference of sets:", sym_diff_set)


print("\nDictionary keys:")

my_dict = {
    'name': 'John',
    'surname': 'Doe',
    'age': 25,
    'city': 'Tbilisi'
}

keys = my_dict.keys()
print("Keys:", keys)


print("\nDictionary values:")

values = my_dict.values()
print("Values:", values)


print("\nAddToDatabase function:")

database = {}

def AddToDatabase(first_name, last_name, age):
    database['first_name'] = first_name
    database['last_name'] = last_name
    database['age'] = age
    print("Updated Database:", database)

AddToDatabase('John', 'Doe', 25)
