from calendar import c
import random

OBJECT_PRONOUNS = ['Her','Him','Them']
POSSESIVE_PRONOUNS = ['Her','His','Their']
PERSONAL_PRONOUNS = ['She','He','They']

STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
         'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']

NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw','Serial Killer', 'Telephone Psychic']

PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
        'Workplace', 'Donut Shop', 'Apocalypse Bunker']

WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']

def main():
    print('Clickbait Headline Generator.')
    print()
    
    print("Our website needs to trick people into looking at ads!")
    while True:
        print("Enter the number of clickbait headlines to generate: ")
        respone = input("> ")
        if not respone.isdecimal():
            print("Please enter number !")
        else:
            numberOfHeadLines = int(respone)
            break
        
    for i in range(numberOfHeadLines):
        clickbaitType = random.randint(1,8)
        
        if clickbaitType == 1:
            headline = generateAreMillennialsKillingHeadLine()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadLine()
        elif clickbaitType == 3:
            headline =generateBigCompaniesHateHerHeadLine()
        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadLine()
        elif clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadLine()
        elif clickbaitType == 6:
            headline = generateGiftIdeaHeadLine()
        elif clickbaitType == 7:
            headline = generateReasonsWhyHeadLine()
        elif clickbaitType == 8:
            headline = generateJobAutomatedHeadline()
            
        print(headline)
    print()
    
    
def generateAreMillennialsKillingHeadLine():
      noun = random.choice(NOUNS)
      return 'Are Millennials Killing the {} Industry?'.format(noun)
        
def generateWhatYouDontKnowHeadLine():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + "s"
    when  = random.choice(WHEN)
    return "Without This {}, {} Could Kill You {}".format(noun, pluralNoun ,when)

def generateBigCompaniesHateHerHeadLine():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choices(NOUNS)
    return "Big Companies Hate {}! See How This {} {} Invented a Cheaper {}".format(pronoun,state,noun1,noun2)

def generateYouWontBelieveHeadLine():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronous = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return "You will not Believe What This {} {} Found in {} {}".format(state,noun,pronous,place)

def generateDontWantYouToKnowHeadLine():
    pluralNoun1 = random.choice(NOUNS) + "s"
    pluralNoun2 = random.choice(NOUNS) + "s"
    return "What {} Do not want you to know about {}".format(pluralNoun1,pluralNoun2)

def generateGiftIdeaHeadLine():
    number = random.randint(7,15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return "{} Gift ideas to give your {} from {}".format(number,noun,state)

def generateReasonsWhyHeadLine():
    number1 = random.randint(3,19)
    pluralNoun = random.choice(NOUNS) + "s"
    number2 = random.randint(1,number1)
    return "{} reasons why {} are more interesting than you think (number {} will surprise you!)".format(number1 , pluralNoun ,number2)

def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    
    i = random.randint(0,2)
    pronouns1 = POSSESIVE_PRONOUNS[i]
    pronouns2 = PERSONAL_PRONOUNS[i]
    if pronouns1 == "Their":
        return "This {} {} did not think robots would take {} job. {} were wrong.".format(state, noun,pronouns1,pronouns2)
    else:
        return "This {} {} did not think robots would take {} job. {} was wrong.".format(state, noun,pronouns1,pronouns2)
    
if __name__ == '__main__':
    main()