import sys
import random

def rps():
	
	#Ask user for what they want
	user = input("What would you like to choose? Rock, Paper, or Scissors? ")
	
	#If user chooses rock
	if user.upper() == "ROCK":
		print("You chose rock.")
		Uanswer = 1
	
	#If user chooses paper
	elif user.upper() == "PAPER":
		print("You chose paper.")
		Uanswer = 2
	
	#If user chooses scissors
	else:
	
		print("You chose paper")
		Uanswer = 3
	
	#Random answer for bot
	bot = int(random.randint(1, 3))
	
	#If bot chooses rock
	if bot == 1:
		print("The Bot chose rock.")
		Banswer = 1
	
	#If bot chooses paper
	elif bot == 2:
		print("The Bot chose paper")
		Banswer = 2
	
	#If bot chooses scissors
	else:
		print("The Bot chose scissors")
		Banswer = 3

	result(Uanswer, Banswer)
	
def result(Uanswer, Banswer):
	
	#Rock vs Rock
	if Uanswer == 1 and Banswer == 1:
		print("Tie!")
	
	#Rock vs Paper
	elif Uanswer == 1 and Banswer == 2:
		print("You lose!")
	
	#Rock vs Scissors
	elif Uanswer == 1 and Banswer == 3:
		print("You win!")
	
	#Paper vs Rock
	elif Uanswer == 2 and Banswer == 1:
		print("You win!")
	
	#Paper vs Paper
	elif Uanswer == 2 and Banswer == 2:
		print("Tie!")
	
	#Paper vs Scissors
	elif Uanswer == 2 and Banswer == 3:
		print("You lose!")
	
	#Scissors vs Rock
	elif Uanswer == 3 and Banswer == 1:
		print("You lose!")
	
	#Scissors vs Paper
	elif Uanswer == 2 and Banswer == 2:
		print("You win!")
	
	#Scissors vs Scissors
	else:
	
		print("Tie!")
	
	again()
	
def again():
	
	#Ask if they would like to play again
	restart = input("Would you like to play again? ")
	
	if restart.upper() == "YES":
		rps()
	
	else:
		main()
	
def main():
	
	#Whether they want to play or not
	start = input("Would you like to start your game of Rock, Paper, Scissors with a bot now? ")
	
	#If yes
	if start.upper() == "YES":
		
		#Start Rock, Paper, Scissors
		rps()
	
	#Quit if no
	else:
		quit() 

main()
