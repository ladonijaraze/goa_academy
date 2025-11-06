def number_sorter():
    print("გამარჯობა! ეს პროგრამა გამოასწორებს რიცხვებს და დაალაგებს მათ.")
    
    
    numbers = input("გთხოვთ, შეიყვანოთ რიცხვები (ცალ-ცალკე გაიმიჯნეთ მომენტით, მაგ: 3 5 1 8): ")
        
        
    number_list = [int(num) for num in numbers.split( )]
        
        
    number_list.sort()
        
    print("დალაგებული რიცხვები:", number_list)
        

    


number_sorter()
