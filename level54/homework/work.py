#1) https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python
def rps(player1, player2):
    
    if player1 == player2:
        return "Draw!"
    
    if player1 == "rock" and player2 == "scissors":
        return "Player 1 won!"
    
    elif player1 == "scissors" and player2 == "paper":
        return "Player 1 won!"
    
    elif player1 == "paper" and player2 == "rock":
        return "Player 1 won!"
    
    else:
        return "Player 2 won!"
#2) https://www.codewars.com/kata/56f3f6a82010832b02000f38/train/python
def describe_age(a):return"You're a(n) "+("kid"if a<13 else"teenager"if a<18 else"adult"if a<65 else"elderly")
#3) https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/python
def sum_array(nums):
    all = 0
    i = 0
    while i < len(nums):
        all += nums[i]
        i += 1
    return all



#4) https://www.codewars.com/kata/5813d19765d81c592200001a/train/python
def dont_give_me_five(start, end):
    count = 0
    for n in range(start, end + 1):
        if '5' not in str(n):
            count += 1
    return count
