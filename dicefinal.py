import random #importing library
money = 250 #starting money amount

print ('Welcome to the dice game!') #printing greeting and instructions
print ('You are given $250 to start')

play_again = 'y'

while play_again == 'y':  #starting of the loop of the game
    bet = input('How much would you like to bet?:') #input for amount of bet
    while int(bet) < 1 or int(bet) > money: #preventing negative money or more money than you have being bet
        print('Invalid bet, please bet within', money)
        bet = input('Please enter valid bet:')
    guess = input('What is your guess on the sum of dice?:') #input for the guess
    print ('Rolling the dice...')
    dice1 = random.randint(1,6) #random number generated between 1 and 6 simulating dice
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2 #sum of both dice
    print ('Dice 1:', dice1, 'Dice 2:', dice2, 'Total:', dice_sum)
    if int(guess) == dice_sum and dice1 == dice2: # total with doubles, tripling the bet
        money = money + int(bet) * 3
        print ('You won! Doubles!:', int(bet) * 3)
        print ('Your current balance is:', money)
    elif int(guess) == dice_sum: #total if winning normally
        money = money + int(bet) * 2
        print ('You won!:', int(bet) * 2)
        print ('Your current balance is:', money)
    else:                                # total if loss
        money = money - int(bet)
        print ('You lose.')
        print ('Your current total is:', money)
    if money == 0:  # ending the game when running out of money
        print('You have run out of money')
        break
    play_again = input('Would you like to continue playing? (y/n)') #beginning to play again loop
    while play_again.lower() not in ['y','n']: #preventing invalid input
        print('Please make a valid choice. y/n')
        play_again = input('Would you like to continue playing? y/n')
            
print('Thank you for playing!')