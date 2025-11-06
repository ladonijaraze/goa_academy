#1
for i in range(1, 51, 2):
    print(i)

#2
size = 5
for i in range(size):
    print("*" * size)

#3
x = 4
y = 6
for i in range(x):
    print("*" * y)

#4
for num1 in range(1, 4):  
    for num in range(1, 4):  
        print(f"num1: {num1}, num: {num}")

#5
print(" mogesalmebit<3")

def registration_form():
    while True:
        username = input("შეიყვანეთ თქვენი username: ")
        if len(username) < 3:
            print("გამოიყენეთ მინიმუმ 3 სიმბოლო.")
            continue
        password = input("შეიყვანეთ თქვენი პაროლი: ")
        if len(password) < 6:
            print("პაროლი უნდა იყოს მინიმუმ 6 სიმბოლო.")
            continue
        email = input("შეიყვანეთ თქვენი email: ")
        if "@" not in email or "." not in email:
            print("გთხოვთ შეიყვანოთ სწორი email.")
            continue
        
        print(f"რეგისტრაცია წარმატებით დასრულდა! {username}!")

registration_form()