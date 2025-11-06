def lalala(num):
    
    ns=num.split(" ")
    arr=[]
    for ragaca in ns:
        arr.append(int(ragaca))
    return f"{max(arr)}{min(arr)}"

print(lalala("12,345,7,78,8,8,9,9,,686,9"))