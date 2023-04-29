import random
number = random.randint(1, 100)
name = input("Hi! What is your name\n")
print('Okay '+name + " Lets Start!")
g = 0  # number of guesses
while (number):
    guess = int(input("Guess the number between 1 and 100!\n"))
    if (guess < number):
        g += 1
        print("Too low!")

    elif (guess > number):
        g += 1
        print("Too high!")

    elif (guess == number):
        g += 1
        break
if (guess == number):
    print("You guessed the number in "+str(g) + " trials!")
