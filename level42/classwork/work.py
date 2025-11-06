#1
def total_points(matches):
    points = 0
    for match in matches:
      
        result = match.split(":")
        our_score = int(result[0])  
        opponent_score = int(result[1])  
        
      
        if our_score > opponent_score:
            points += 3 
        elif our_score < opponent_score:
            points += 0 
            points += 1 
            
            
    return points
#2
"15/2"
"ნაშთი 1-1"
'7/2'
"ნაშთი 2-1"
'3/2'
"ნაშთი 3-1"
'1/2'
"ნაშთი 4-1"
my_age=1111
#2
#def gamotvla():
 #   input=int(number)
 #    result_1=number%2
  #  result_2=(number/2)%2
   # result_3=((number//2)//2)%2

    #print("----------------")
    #print(result_1)
    #rint(result_2)
    #print(result_3)
#gamotvla()
#2
age = 14
binary_age = ""

while age > 0:
    binary_age = str(age % 2) + binary_age
    age = age // 2

#3
def fake_bin(x):
    result = []
    
   
    for digit in x:
       
        if int(digit) < 5:
            result.append('0')  #
        else:
            result.append('1') 
    
 
    return ''.join(result)
