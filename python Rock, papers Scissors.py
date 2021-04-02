import random

comp_wins = 0
user_wins = 0


# Why do i need to put in this first bit comp_wins and users wins = 0???

def Choose_Option() :
    user_choice = input ("Please input either R,P or S (Rock, Paper or Scissors respectively:")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "P"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print ("Please ONLY choose R,P or S.")
    return user_choice

# Change the print prompt error of user choice. Maybe use drop down menu or more description for the users

# Is there a better way to write this code or is this basic for newbies

def Computer_Option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"  
    else:
        comp_choice = "s"
    return comp_choice

while True:
    print("")
    user_choice = Choose_Option()
    comp_choice = Computer_Option()
    print("")

# Why do i need to use the "while true" here?

    if user_choice == "r":
        if comp_choice == "r":
            print("Your rock vs Computers rock. You've tied")
            
        elif comp_choice == "p":
            print("Your rock vs Computers paper. You've lost")
            comp_wins +=1
            
        elif comp_choice == "s":
            print("Your rock vs Computers scissors. You've won!")
            user_wins +=1

    if user_choice == "p":
        if comp_choice == "r":
            print("Your paper vs Computers rock. You've won!")
            user_wins +=1
            
        elif comp_choice == "p":
            print("Your paper vs Computers paper. You've tied")
            
        elif comp_choice == "s":
            print("Your paper vs Computers scissors. You've lost")
            comp_wins +=1

    if user_choice == "s":
        if comp_choice == "r":
            print("Your scissors vs Computers rock. You've lost")
            comp_wins +=1
            
        elif comp_choice == "p":
            print("Your scissors vs Computers paper. You've won!")
            user_wins +=1
            
        elif comp_choice == "s":
            print("Your scissors vs Computers scissors. You've tied")

    print("")
    print("Player wins: " + str(user_wins))
    print("Computer wins: " + str(comp_wins))
    print("")

    user_choice = input ("do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break
    
 # Problem if there is a space with the answers (i.e " Y") Is there a better way to do it?
 
 # Need an ultimate ending text saying overall "overall you win or lose (with the numbers of wins/losses). thank you for playing"
 
 # a restart to fully restart the game even start from 0,0 wins and losses (if break can i restart?) 
