import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

name = input('What is your name? ')
print('Hello ' + name + ', think of a number between 1 and 15.')
print('Can you guess the number I am thinking of?')
print('I will give you 5 guesses.\n')

play_again = ''

while (play_again != 'n' and play_again != 'no'):
    rand = random.randint(1,15)
    guesscount = 0

    while guesscount != 5:
        print("\nWhat is your numerical guess? ")
        number = input()
        number = int(number)
        guesscount += 1
        
        if number > rand:
            print('Your guess was too high, You have guessed {guesscount} times.'.format(guesscount=guesscount))

        if number < rand:
            print('Your guess was too low, You have guessed {guesscount} times.'.format(guesscount=guesscount))

        if number == rand:
            break
    if number == rand:
        guesscount= str(guesscount)
        print('Correct! It took you '+ guesscount +' guesses! ')
    if number != rand:
        print('\n')
        rand = str(rand)
        print('\nSorry I was thinking of the number ' + rand + '.' )
    
    play_again = input("\nDo you want to play again and guess a different number? (yes or no): ").lower().strip()
    

print('\nThat sucks, but here is a question for the road.')

#Bonus prompt if the user does not want to play again below

############################################################
############################################################
############################################################
############################################################

color = ''
while(color != 'cream and crimson'):
    color = input("\nWhat are IU's school colors? ")
    color = color.lower().strip()
    if (color == 'cream and crimson'):
        break
    else:
        print("Incorrect the colors are Cream and Crimison, but thanks for playing!")
        break
if (color == 'cream and crimson'):
    print("You got it! Go IU!")
    print("\U0001F606") #Searched Unicode for this emoji!










    
        

    






    





    




