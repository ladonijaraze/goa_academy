# მომხმარებლის მონაცემებზე იმუშავა ბატონმა
user1 = {
    "name": "John",
    "surname": "Doe",
    "bornYear": 1990,
    "password": "password123",
    "email": "john.doe@example.com",
    "cards": [
        ["masstercard", 40, "usd"],
        ["amex", 100, "gel"]
    ]
}

user2 = {
    "name": "Jane",
    "surname": "Smith",
    "bornYear": 1985,
    "password": "password456",
    "email": "jane.smith@example.com",
    "cards": [
        ["visa", 50, "usd"],
        ["mastercard", 200, "gel"]
    ]
}
#კარტის დამატებაზე და მის აღებაზე იმუშავა ბატონმა
def add_card(user, card_type, balance, currency):

    user["cards"].append([card_type, balance, currency])

def get_card(user, card_index):

    if 0 <= card_index < len(user["cards"]):
        return user["cards"][card_index]
    else:
        print("Invalid card index.")
        return None
    
# თანხის გადამოწმება დოლარის კურსი და ასე შემდეგ იმუშავა  ბატონმა  და ბატონმა  ,ცოტა ბევრის წერა მოგვიწია😅😅 

def transfer_funds(from_user, to_user, from_card_index, to_card_index, amount):
    from_card = get_card(from_user, from_card_index)
    to_card = get_card(to_user, to_card_index)

    if not from_card or not to_card:
        print("Invalid card index.")
        return 

    if from_card[1] >= amount:
        from_card[1] -= amount 
        to_card[1] += amount    
        print("Transfer successful: " + str(amount) + " " + from_card[2] + " from " + from_user["name"] + " to " + to_user["name"])
    else:
        print("Insufficient funds.")

def convert_currency(amount, from_currency, to_currency):

    conversion_rates = {
        ('gel', 'usd'): 0.38,
        ('usd', 'gel'): 2.63
    }
    
    if from_currency == to_currency:
        return amount

    if (from_currency, to_currency) in conversion_rates:
        return amount * conversion_rates[(from_currency, to_currency)]
    else:
        print("Conversion not available between " + from_currency + " and " + to_currency + ".")
        return None

def transfer_with_conversion(from_user, to_user, from_card_index, to_card_index, amount, from_currency, to_currency):
    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        transfer_funds(from_user, to_user, from_card_index, to_card_index, converted_amount)
        print("Amount " + str(amount) + " " + from_currency + " converted to " + str(converted_amount) + " " + to_currency)
    else:
        print("Conversion failed.")

# მომხმარებლის მონაცემების შემოწმებაზე იმუშავა ბატონმა
add_card(user1, "masstercard", 40, "usd")
add_card(user1, "amex", 100, "gel")

add_card(user2, "visa", 50, "usd")
add_card(user2, "mastercard", 200, "gel")

print("User1 data:", user1)
print("User2 data:", user2)


transfer_funds(user1, user2, 0, 0, 10)  

transfer_with_conversion(user1, user2, 1, 0, 50, "gel", "usd")  
