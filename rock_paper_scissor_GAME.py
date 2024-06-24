import random
system = 0
user = 0
def game(number):
    global system, user  
    options = ["rock", "paper", "scissor"]
    for i in range(number):
        user_choice = input("Enter your option (rock, paper, scissor) or 'exit' to quit: ").lower()
        if user_choice == "exit":
            return
        elif user_choice not in options:
            print("Invalid choice, please try again.")
            continue
        
        system_choice = random.choice(options)
        print(f"System choice: {system_choice}")
        if user_choice == "rock" and system_choice == "paper":
            print("System won")
            system += 1
        elif user_choice == "paper" and system_choice == "scissor":
            print("System won")
            system += 1
        elif user_choice == "scissor" and system_choice == "rock":
            print("System won")
            system += 1
        elif user_choice == system_choice:
            print("Draw")
        else:
            print("User won")
            user += 1
        scores()
        
            
def scores():
    print ("user score",user)
    print("system score",system)
    if user>system:
        print("CONGRATULATIONS")
    elif system>user:
        print("BETTER LUCK NEXT TIME")
    elif user==system:
        print("TOUGH COMPETITION")

def main():  
    try:
        number = int(input("Enter the number of rounds you want to play: "))
        game(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    
if __name__ == "__main__":
    main()