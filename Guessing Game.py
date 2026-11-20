'''5. Number Guessing Game 
Beginner 
Concepts: while, if-else, functions 
Requirements 
• Generate a random number from 1 to 100. 
• Ask the player to guess the number. 
• Display “Too high” or “Too low.” 
• Limit the player to seven attempts. 
• Display the final result. 
Bonus: Add easy, medium, and hard difficulty levels with different attempt limits. '''



def game():
    import random
    def random1():
        num = random.randint(1,100)           
        return num
    while True:
        print("\n     WELCOME TO THE GUESSING GAME     ")
        choice = input("Would you  like to guess the number(y/n) :  ")
        if choice == "n":
            print("Thank You!")
            break
        
        elif choice == "y":
            print("1. Easy Level")
            print("2. Medium Level")
            print("3. Hard Level")
            level = input("Enter your choice: ")
            if level == "1":
                number = random1()
                attempts = 5
            elif level == "2":
                number = random1()
                attempts = 3
            elif level == "3":
                number = random1()
                attempts = 2
            else:
                print("Invalid Choice!")
                continue
            count = 1
            while count <= attempts:
                print(f"\nAttempt {count}/{attempts}")
                guess = int(input("Enter your number: "))
                if guess == number:
                    print("Congratulations! You guessed it correctly.")
                    break
                elif guess > number:
                    print("Too High!")
                else:
                    print("Too Low!")
                count += 1
                if count > attempts:
                    print("Game Over!")
                    print("The correct number was:", number)
                    break
            else:
                print("Invalid Choice!")

game()
