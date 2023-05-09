#supermarket billing using while true



while True:
    name = input("Enter Your name : ")
    total = 0
    
    while True:
        print("Enter amount and quantity")
        amount = float(input("Enter amout: "))
        quantity = float(input("Enter Quantity"))
        total += amount * quantity

        repeat = input("Do you want to add more ? ")
        if repeat =="no":
            break
        
    print("-"*40)
    print("Custormer name ",name)
    print("Customer total", total)
    print("-"*40)
        
    repeat1 = input("next cx? ")
    if repeat1 =="no":
        break
