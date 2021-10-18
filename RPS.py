# Author: Arsene Bwasisi
# Description: Open this file on your computer terminal and play game
#              of rock, paper, scissors with the program! 

import random

def game(choices, score1=0, score2=0):

	print("First to three points wins!")
	print("Ready?")

	while score1 < 3 and score2 < 3:
		choice = input("Insert choice here: ").lower()
		idx = random.randint(0, 2)
		print(choices[idx])

		if idx == 0:
			if choice == 'paper':
				score1 += 1
				print("One point for you! Good job!")
			elif choice == 'scissors':
				score2 += 1
				print("That's one point for me!")
			else:
				print("Score remains the same.")
		elif idx == 1:
			if choice == 'scissors':
				score1 += 1
				print("One point for you! Good job!")
			elif choice == 'rock':
				score2 += 1
				print("That's one point for me!")
			else:
				print("Score remains the same.")
		elif idx == 2:
			if choice == 'rock':
				score1 += 1
				print("One point for you! Good job!")
			elif choice == 'paper':
				score2 += 1
				print("That's one point for me!")
			else:
				print("Score remains the same.")
				

	return score1, score2


name = input("Hello, what's your name?: ")
print("Hi", name.title() + '!')
print("Would you like to play a quick game of Rock, Paper, Scissors?")
play_game = input("y/n: ")

while play_game == 'y':

	choices = ['rock', 'paper', 'scissors']
	score1, score2 = game(choices)


	if score1 == 3:
		print('Congrats! You beat me!')
		play_game = input("Would you like to go again? (y/n): ")
	else:
		print('Looks like I won.')
		play_game = input("Would you like to go again? (y/n): ")

print("It was nice meeting you", name.title() + '.')
