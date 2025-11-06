#1
number = int(input("შეიყვანეთ რიცხვი: "))

if number < 10:
    print("რიცხვი 10-ზე ნაკლებია.")
else:
    print("რიცხვი 10 ან მეტი არის.")
#2
number = int(input("შეიყვანეთ რიცხვი: "))

if number % 2 == 0:
    print("რიცხვი ლუწია.")
else:
    print("რიცხვი ლუწი არ არის.")
#3
number = int(input("შეიყვანეთ რიცხვი: "))

if number > 0:
    print("რიცხვი დადებითია.")
elif number == 0:
    print("რიცხვი ნულია.")
else:
    print("რიცხვი უარყოფითია.")
#4
number1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
number2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

if number1 == number2:
    print("რიცხვები ტოლია.")
else:
    print("რიცხვები არ არის ტოლი.")
#5
number = int(input("შეიყვანეთ რიცხვი: "))

if number > 100 and number % 2 == 0:
    print("რიცხვი 100-ზე მეტია და ლუწია.")
else:
    print("რიცხვი ან 100-ზე ნაკლებია, ან ლუწი არაა.")
#5
number = int(input("შეიყვანეთ რიცხვი: "))

if number % 5 == 0 or number % 10 == 0:
    print("რიცხვი არის 5-ის ან 10-ის ჯერადი.")
else:
    print("რიცხვი არ არის 5-ის ან 10-ის ჯერადი.")
