total_cost = 0.0
print("WELCOME TO OUR GROCERY SHOP")
print("Enter the price of each item. Type 0 when you are finished.\n")
print("-------------------------------")

while True:
    price = float(input("Enter item price: = "))
    
    if price == 0:
        break
        
    total_cost += price
    print("-------------------------------")
print(f"Your total cost list is: ${total_cost:.2f}")