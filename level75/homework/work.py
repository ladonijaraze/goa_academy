def make_repeater(n):
    def repeater(text):
        return text * n
    return repeater

repeat5 = make_repeater(5)
print("Task 1:", repeat5("გოა"))


def bank_account(initial_balance):
    balance = initial_balance

    def withdraw(amount):
        nonlocal balance
        balance -= amount
        print("Remaining:", balance)

    return withdraw

acc = bank_account(100)
print("Task 2:")
acc(20)
acc(30)

def power_of(base):
    def power(exponent):
        return base ** exponent
    return power

base_two = power_of(2)
print("Task 3:", base_two(3))

points = 10

def add_point():
    global points
    points += 1
    print(points)

print("Task 4:")
add_point()


def calculate_rectangle_area(a, b):
    return a * b

print("Task 5:", calculate_rectangle_area(5, 10))

logs = []

def add_log(message):
    logs.append(message)

add_log("First log")
add_log("Second log")
print("Task 6:", logs)


def calculate_tax(tax_rate):
    def tax(price):
        return price * tax_rate
    return tax

georgian_tax = calculate_tax(0.18)
print("Task 7:", georgian_tax(100), georgian_tax(250))



name = "Global"

def show_name():
    name = "Local"
    print("Inside:", name)

print("Task 8:")
show_name()
print("Outside:", name)


def make_prefix(prefix):
    def add_prefix(name):
        return prefix + name
    return add_prefix

dr_prefix = make_prefix("Dr. ")
print("Task 9:", dr_prefix("Davit"))



numbers = [1, 5, 8, 10, 15, 20]
result = list(filter(lambda x: x % 5 == 0, numbers))
print("Task 10:", result)