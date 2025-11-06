#1
for i in range(1, 51, 2):
    print(i)
#2
size = 2  
for i in range(size):
    print("*" * size)
#3
width = 7 
height = 4 

for i in range(height):
    print("*" * width)
#4
for num1 in range(1, 4):  
    for num in range(1, 4):
        print(f"num1: {num1}, num: {num}")
#5
print("გამარჯობა! დაასრულეთ რეგისტრაცია.")


while True:
    username = input("მიუთითეთ თქვენი სახელი ")
    if len(username) < 3:
        print("სახელი უნდა იყოს მინიმუმ 3 სიმბოლო.")
        continue
    break

while True:
    password = input("მიუთითეთ თქვენი პაროლი: ")
    if len(password) < 6:
        print("პაროლი უნდა იყოს მინიმუმ 6 სიმბოლო.")
        continue
    break

while True:
    confirm_password = input("გაიმეორეთ პაროლი: ")
    if confirm_password != password:
        print("პაროლები არ ემთხვევა. სცადეთ ისევ.")
        continue
    break

print("რეგისტრაცია დასრულდა! კეთილი იყოს თქვენი მობრძანება, " + username + "!")