def mgeli(*zagli,gela,**mgeli):
    print(zagli)
    print(mgeli)
    print(gela)


mgeli(1,2,3,4,53,gela="private island",ladoa="jeff")



class age:
    g=24

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

new=person("lado",15)
print(new.name)
print(new.age)


print("__________________________________")


class animals:
    def __init__(self,name,age,color,jeision_born):
        self.name=name
        self.age=age
        self.color=color
        self.jeision_born=jeision_born


an=animals("gori",4,"shavi",False)

print(an.name)
print(an.age)
print(an.color)
print(an.jeision_born)
