import random
name = input("Enter your Name: ")
print('Hello! '+name+' lets start the Game.')
print('Entered choice must be in lowercase')
while True:
    ls = ['rock', 'paper', 'scissor']
    guess = input("Enter your choice: ")
    c = random.choice(ls)
    if (c == guess):
        print('You Win')
    if (c != guess):
        print("You lose")
    print('Press enter to exit game or Any other key from keyboard to play more!')
    play = input("Enter your choice: ")
    if (play == ""):
        print('You have exited the game')
        break
    else:
        print('Play new game!')
