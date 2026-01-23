#https://www.codewars.com/kata/568dc014440f03b13900001d/train/python
def get_drink_by_profession(param):
    drinks = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal"
    }

    return drinks.get(param.lower(), "Beer")

#https://www.codewars.com/kata/586f61bdfd53c6cce50004ee/train/python
def user_contacts(data):
    result = {}

    for user in data:
        name = user[0]
        zip_code = user[1] if len(user) > 1 else None
        result[name] = zip_code

    return result

#https://www.codewars.com/kata/5a360620f28b82a711000047/train/python
def define_suit(card):
    suits = {'S': 'spades', 'D': 'diamonds', 'H': 'hearts', 'C': 'clubs'}
    return suits[card[-1]]

#https://www.codewars.com/kata/5827bc50f524dd029d0005f2/train/python
def get_first_python(list_of_devs):
    for dev in list_of_devs:
        if dev['language'] == 'Python':
            return f"{dev['first_name']}, {dev['country']}"
    return "There will be no Python developers"

#https://www.codewars.com/kata/53da6a7e112bd15cbc000012/train/python
def sort_dict(d):
    items_list = list(d.items())

    n = len(items_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items_list[j][1] < items_list[j + 1][1]:
                items_list[j], items_list[j + 1] = items_list[j + 1], items_list[j]

    return items_list
