import random

random_number=random.randint(1,20) #generate a random number and store it in "random_number"
def sameno(target,number): #create function 'sameno' that compares 2 arguments 'target' and 'number'
	if target == number:
		result = "win"

	elif target > number:
		result = "small"

	else:
		result = "big"

	return result

guessesTaken = 0
score = 100

print("\nLet's play 'Guess a number from 1 to 20'. You have 5 tries\n")

while guessesTaken < 5:
	user_guess=int(input("Your guess: "))
	guessesTaken = guessesTaken + 1
	tries = 5 - guessesTaken 
	high_or_low=sameno(random_number, user_guess) # store the result of the function in a variable 'high_or_low'

	if high_or_low == "win":
		print("\nWell done, number was:"+str(random_number)+"\nYou won with a score of: " + str(score))
		guessesTaken = 5

	elif high_or_low == "small":
		score = score - 20
		print("Number is too small. You have "+str(tries)+" tries left and your score is now "+str(score))
	
	else: 
		score = score - 20
		print("Number is too big. You have "+str(tries)+" tries left and your score is now "+str(score))

if high_or_low == "win":
	print("Bye!")		
else:
	print("you loose ! The number was "+ str(random_number))
