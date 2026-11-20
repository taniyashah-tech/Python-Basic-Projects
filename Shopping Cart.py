'''6. Shopping Cart and Checkout 
Intermediate 
Concepts: Loops, conditions, functions, lists, dictionaries 
Requirements 
• Store products and prices. 
• Allow customers to add items and quantities. 
• Calculate item-wise and total costs. 
• Apply discounts based on purchase value. 
• Generate a final bill. 
Bonus: Implement removing an item and checking product availability. '''


def shopping():
    products = { 
            "Rice"        : 60,
            "Wheat Flour" : 45,
            "Sugar"       : 50,
            "Milk"        : 30,
            "Bread"       : 40,
            "Biscuits"    : 20,
            "Tea Powder"  : 120,
            "Coffee"      : 180,
            "Cooking Oil" : 150,
            "Soap"        : 35,
            "Shampoo"     : 90,
            "Toothpaste"  : 70,
            "Chips"       : 25,
            "Cold Drink"  : 45,
            "Chocolate"   : 50,
            "Mouse"       : 500,
            "Keyboard"    : 1000,
            "Headphones"  : 1500,
            "Speaker"     : 2500,
            "Pendrive"    : 700,
             "Webcam"      : 1800,
             "Monitor"     : 12000,
             "Laptop"      : 50000
        }
    cart = {}
    while True:
        print("\nWelcome to the SMART-BAZAAR ")
    
        i = 1
        for item,price in products.items():
            print(f"{i}.{item} : {price}")
            i+=1
        
        product_list = list(products.keys())
        choice = int(input("Enter Product Number : "))
        if 1<= choice <= len(product_list):
            product_name = product_list[choice - 1]
            
            quantity = int(input("Enter Product Quantity : "))
            
            if product_name in cart:
                cart[product_name] += quantity
            else:
                cart[product_name] = quantity
            check = input("Want to add more items(y/n) : ")
            if check == "n":
                break
        else:
            print("This Product is not Available! ")
            continue
    total_price = []
    for key, value in products.items():
        if key in cart :
            item_total = value * cart[key]
            total_price.append(item_total)
    total_bill = sum(total_price)
    item_total = 0
    if total_bill >= 15000:
        discount = (total_bill * 20) / 100
    elif total_bill >= 5000 :
        discount = (total_bill* 10) / 100
    else:
        discount = 0
    after_discount = total_bill - discount
    
    name = input("Please enter your name : ")
    print("\n             SMART-BAZAAR     ")
    print("-------------------------------------------------")
    print(f"Name : {name}              Date : 27/10/26")
    print("\ns.no\tItems\t\tQty\tPrice\tTotal")
    s = 1
    for key, value in cart.items():
            quantity = value
            price = products[key]
            item_total = quantity * price
            
            print(f"\n{s}\t{key}\t\t{quantity}\t{price}\t{item_total}")
            
            s += 1
            
    print("-------------------------------------------------")
    print(f"Total Bill : {total_bill}Rs")
    print(f"Discount   : {discount}Rs")
    print(f"Final Bill : {after_discount}Rs")
    print("-------------------------------------------------")
    print("\n      Thank You\n      Visit Again")
    
shopping()
