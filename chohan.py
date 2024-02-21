import random , sys 

JAPANESE_NUMBER = { 1: 'ICHI' , 2:'NI' , 3:'SAN',
                   4: 'SHI' , 5: 'GO', 6:'ROKU'}

print('''In this traditional Japaness dice game, two dice are rolled 
      in a bamboo cup by the dealer sitting on the floor. 
      The player must guess if the dice total to an even(cho) or
      odd(han) number.''')

purse = 5000

while True:
    print("You have ", purse, "mon.How much do you bet?(or QuiT)")
    while True:
        pot = input('> ')
        if pot.upper()== "QUIT":
            print("Thank for playing!")
            sys.exit()
        elif int(pot) > purse:
            print("You do not have enough to make that bet.")
            print("How much you want to bet.")
        else:
            pot = int(pot)
            break
    
    #roll the dice
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    print("The dealer swirls the cup and you hear the rattle of dice.")
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print("     CHO(even) or HAN(odd)?")
    
    #let the player bet cho or han
    while True:
        bet = input('> ').upper()
        if bet !='CHO' and bet !='HAN':
            print("Please enter either 'CHO' or 'HAN'.")
            continue
        else:
            break
    #reveal the dice results:
    print('The dealer lifts the cup to reveal:v')
    print('  ',  JAPANESE_NUMBER[dice1], '-', JAPANESE_NUMBER[dice2])
    print('    ',dice1, '-', dice2)
    
    #determine if the player won:
    rollsEnven = (dice2 + dice1) %2 == 0
    if rollsEnven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'
        
    playerWon = bet == correctBet
    if playerWon:
        print("You won! You take",pot , 'mon.')
        purse = purse + pot
        print("The house collects a ", pot //10 , 'nom fee.')
        purse = purse - (pot //10) # the house fee if 10%
    else:
        purse = purse - pot #subtract the pot from player purse.
        print('YOU LOST!')
        
    if purse == 0:
        print("You have ran out of money.\nThanks for playing!.")
        sys.exit()
            