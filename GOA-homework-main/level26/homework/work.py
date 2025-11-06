#1
from turtle import*


def draw_triangle(side_length):
    for _ in range(3):
        forward(side_length)
        left(120)

def მოქმედება():
    speed(0)  
    side_length = 50  
    for i in range(1, 121, 2):  
        penup()
        goto(i * 10, i * 10)  
        pendown()
        if i % 2 != 0:  
            color("green")  
        else:
            color("blue")  
        draw_triangle(side_length)
        
        done()

მოქმედება(120)
#2
def hello_world():
    print("print()")


hello_world()

#3
def even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} არ არის კენტი")
    else:
        print(f"{number} კი არის კენტი")

even_or_odd(23)  
#4
def ფიფქები():
    patterns = [
        "******\n******\n******",  
        "     *\n    ***\n  *******\n***********\n     *\n     *",  
        "*******\n *******\n  ********\n    ********"  
    ]
    
    for _ in range(120):
        for pattern in patterns:
            print(pattern)
            print("\n" + "-"*20 + "\n")  

ფიფქები()

