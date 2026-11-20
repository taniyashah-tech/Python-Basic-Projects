'''4. Restaurant Billing System 
Beginner–Intermediate 
Concepts: Loops, conditions, functions 
Requirements 
• Display a menu with item prices. 
• Let customers select items and quantities. 
• Calculate the running bill. 
• Apply discounts based on the bill amount. 
• Calculate the final bill, including tax. 
Bonus: Add coupon codes and repeat-order functionality. '''

def restraunt():
    def display():
        menu = [
            "1.Pizza : 150rs",
            "2.Pasta : 200rs",
            "3.Corn-Dog : 100rs",
            "4.Dosa : 120rs",
            "5.Idli Sambher : 50rs",
            "6.Cold Drink : 35rs"
        ]
        
        for item in menu:
            print(item)

    def bill(price,quantity):
        return price * quantity

    def discount(total_bill):
        if total_bill >= 1000:
            discount = (total_bill * 20) / 100
           
        elif total_bill >= 500:
            discount = (total_bill * 10) / 100
            
        else:
            discount = 0
        
        return discount

    def tax(after_discount):
        return (after_discount * 5)/100
            
            
    name = input("please Enter your name : ")
    total_bill = 0
    
    while True:
        
        display ()
        
        items = input("Please! Select your items...")
        quantity = int(input("Enter quantity..."))
        
        if items == "1":
            price = 150
        elif items == "2":
            price = 200
        elif items == "3":
            price = 100
        elif items == "4":
            price = 120
        elif items == "5":
            price = 50
        elif items == "6":
            price = 35
        else:
            print("Invalid Items...")
            continue
        
        items_bill = bill(price,quantity)
        total_bill += items_bill
       
        order = input("would you like to order more?(y/n)")
        if order  in "Yy":
            pass
        elif order in "Nn":
            break
        else:
            print("Invalid Text..Try again...!")
            continue

        
    discount_amount = discount(total_bill)
    after_discount = total_bill - discount_amount
    tax_amount = tax(after_discount)
    final_bill = after_discount + tax_amount

    coupon = input("Do you want to use coupon (y/n) : ") 
    if coupon == "y":
        code = input("enter code : ")
        if code == "save10" and final_bill >= 300:
            final_bill -= (final_bill * 10)/100
            print("Coupon Applied Succesfully...!")
        else:
            print("wrong Code..")
    elif coupon == "n":
        print("No coupon is Applied")
    else:
        print("Invalid Code")
        


    print("          -YOUR BILL-          ")
    print(f"{name}            Date : 25/10/2k26")
    print("--------------------------------")
    print(f"Total Bill : {total_bill}")
    print(f"Discount : {discount_amount}")
    print(f"tax : {tax_amount}")
    print(f"Final Bill : {final_bill}")
    print("--------------------------------")
    print("          THANK-YOU!\n      VISIT AGAIN....          ")

restraunt()
