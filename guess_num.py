import random

name = input("Hello, what's your name?: ")
print("Hi", name.title() + '!')
number = input("What's your favorite number?: ")
print("Nice choice!")
print(name.title(), "would you like to play a quick game?")
play_game = input("y/n: ")

while play_game == 'y':
	shots = 0
	num = random.randint(1, 10)

	print("I'm thinking of a number between 1 and 10.")
	print("You have 3 shots")

	while shots < 3:
		shots += 1
		guess = int(input("Guess the number: "))

		if guess == num:
			print("Well done! You got it right.")
			print("would you like to play another round?")
			play_game = input("y/n: ")

			if play_game == 'n':
				print("Thank you for playing!")	

			break	
		else:		
			if shots != 3:
				print("Wrong number. Try again.")
			else:
				print("You shots have ran out! The number was", num)	
				print("would you like to play another round?")
				play_game = input("y/n: ")

				if play_game == 'n':
					print("Good try! Thank you for playing!")

				break

print("It was nice meeting you", name.title() + '.')	
