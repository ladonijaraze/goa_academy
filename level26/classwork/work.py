from turtle import*
def walk():
    forward(200)
    left(90)
    width(8)
    

def back():
    left(90)
    forward(200)
    width(8)

def lala():
    walk()
    back()


lala()

exitonclick()