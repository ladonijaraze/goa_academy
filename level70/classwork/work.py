#Fill in the blanks to create a list of numbers multiplied by 10 in the range of 5 to 9.
a = [x*10 for x in range(5, 9)]


#def nugo(n):
 #   if n%2==0:
#        return n
#
#saboloo=(list(map(nugo,[12,33,44,66,77])))

def nugo(n):
    return n % 2 == 0

saboloo = list(filter(nugo, [12, 33, 44, 66, 77]))
print(saboloo)