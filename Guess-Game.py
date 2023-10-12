#Welcome to the math guessing game made by Dineth Gimhana : Github(DinethGR)
#===========================================================================

#print welcome massage to players
print("Welcome To The Math Guessing Game")

#Enter the input for starting guessing game
G = input("Enter The Number:")

#Input assign to string 
Guess = int(G)

#Condition-1
if Guess == 5:
    print("Congratulation...!")
    print("You Win..!")

#Condition-2
else:
    print("Oops...")
    print("You Lose..!")
    print("Try Again..")

#Thanks for plyaing this game
print("<<<< GAME OVER >>>>")

#=========================================================================