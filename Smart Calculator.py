'''1. Smart Calculator 
Beginner 
Concepts: if-elif-else, while, functions 
Requirements 
• Display a menu for addition, subtraction, multiplication, division, and modulus. 
• Take two numbers from the user. 
• Use separate functions for each operation. 
• Handle division by zero. 
• Repeat until the user selects Exit. 
Bonus: Add power and floor division operations. '''

def calculator():

    def add(num1,num2):
        return num1 + num2

    def sub(num1,num2):
        return num1 - num2
        
    def mul(num1,num2):
        return num1 * num2
        
    def div(num1,num2):
        if  num2 == 0:
            return "Error : Division By Zero"
        else:
            return num1/num2

    def mod(num1,num2):
        if num2 == 0:
            return "Error : Modulus By Zero"
        else:
            return num1%num2

    def power(num1,num2):
        return num1 ** num2

    def floordiv(num1,num2):
        if  num2 == 0:
            return "Error : FloorDiv By Zero"
        else:
            return num1 // num2


    while True:
        print("----Calculator----")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Modulus")
        print("6.Power")
        print("7.Floor Division")
        print("8.Exit")

        choice = input("Please Enter Your Choice : ")
        
        if choice == "8":
            print("Thank You!")
            break
        
        if choice not in "1234567":
            print("Invalid Choice!")
            continue
        
        num1 = int(input("Enter the 1st number : "))
        num2 = int(input("Enter the 2nd number : "))
        
        if choice == "1":
            print(f"Addition : {add(num1,num2)}")
        elif choice == "2":
            print(f"Subtraction : {sub(num1,num2)}")
        elif choice == "3":
            print(f"Multiplication : {mul(num1,num2)}")
        elif choice == "4":
            print(f"Division : {div(num1,num2)}")
        elif choice == "5":
            print(f"Modulus : {mod(num1,num2)}")
        elif choice == "6":
            print(f"Power : {power(num1,num2)}")
        elif choice == "7":
            print(f"Floor Div : {floordiv(num1,num2)}")
        
        
calculator()   
    
    
