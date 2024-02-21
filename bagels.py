import random

Num_Digit = 3
Max_Guesses = 10

def main():
    print('''Bagels, a dedutive logic  game.
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:     That mean:
        Pico        One digit is correct but in the wrong position.
        Fermi       One digit is correct and in the right position.
        Bagels      No digit is correct.
        
    For example, if the secret number was 248 and your guess was 843,
    the clues would be Fermi Pico. '''.format(Num_Digit))
    while True:
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print("You have {} guesses to get it.".format(Max_Guesses))

        numGuesses = 1
        while numGuesses <= Max_Guesses:
            guess = ""
            while len(guess) != Num_Digit or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses +=1

            if guess == secretNum:
                break
            if numGuesses > Max_Guesses:
                print("You ran out of Guesses.")
                print("The answer was {}.".format(secretNum))

        print("Do you want to play again?(y/n)")
        if not input("> ").lower().startswith('y'):
            break
    print("Thank you for playing!")

def getSecretNum():
    numbers = list("0123456789")
    random.shuffle(numbers)
    secretNum = ''
    for i in range(Num_Digit):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess ,secretNum):
    if guess == secretNum:
        return "You got it!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    
    if len(clues) ==0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()


