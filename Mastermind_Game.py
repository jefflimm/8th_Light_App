#Game intro + rules
print "- Welcome to Tetrachrome -"
print
print "By: Jeffrey C. Lim"
print
print "A game between man and machine."
print 
print "Man will choose a color code and machine will have 10 guesses."
print
print "Please choose four colors from below:"
print "[ red | green | orange | yellow | blue | purple ]"
print

#Setting up the game human input
choices = ["red", "green", "orange", "yellow", "blue", "purple"]

color_1 = raw_input("Choose your first color: ").lower()
while True:
	if color_1 in choices:
		break
	else:
		print
		print "This is not one of your choices"
		print
		color_1 = raw_input("Choose your first color: ").lower()
		
color_2 = raw_input("Choose your second color: ").lower()
while True:
	if color_2 in choices:
		break
	else:
		print
		print "This is not one of your choices"
		print
		color_2 = raw_input("Choose your second color: ").lower()
		
color_3 = raw_input("Choose your third color: ").lower()
while True:
	if color_3 in choices:
		break
	else:
		print
		print "This is not one of your choices"
		print
		color_3 = raw_input("Choose your third color: ").lower()

color_4 = raw_input("Choose your last color: ").lower()
while True:
	if color_4 in choices:
		break
	else:
		print
		print "This is not one of your choices"
		print
		color_4 = raw_input("Choose your last color: ").lower()

answers = [color_1, color_2, color_3, color_4]

#verifying the code
print
print "Your Code:" 
print "[", color_1,"|", color_2,"|", color_3,"|", color_4, "]"

#Computer's turn
import random

comp_guess = 10

while comp_guess > 0:
	guess_1 = random.choice(choices)
	if guess_1 in answers:
		guess_2 = random.choice(choices)
		if guess_2 in answers:
			guess_3 = random.choice(choices)
			if guess_3 in answers:
				guess_4 = random.choice(choices)
				if guess_4 in answers:
					print
					print "The computer has guessed correctly!"
					print "Number of guesses taken:", comp_guess
					print
					print "- Thank you for playing!!! -"
					break
				else:
					choices.remove(guess_4)
					comp_guess -= 1
			else:
				choices.remove(guess_3)
				comp_guess -= 1
		else:
			choices.remove(guess_2)
			comp_guess -= 1
	else:
		choices.remove(guess_1)
		comp_guess -= 1
else:
	print "The computer has guessed incorrectly!"



