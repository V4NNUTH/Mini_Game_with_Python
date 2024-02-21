
import datetime , random

def getBirthday(numberOfBirthday):
    birthdays =[]
    for i in range(numberOfBirthday):
        startOfYear = datetime.date(2001,1,1)

        randomNumberOfDay = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear +randomNumberOfDay
        birthdays.append(birthday)
    
    return birthdays

def getMarch(birthdays):
    if len(birthdays) ==len(set(birthdays)):
        return None

    for a ,birthdayA in enumerate(birthdays):
        for b,birthdayB in enumerate(birthdays[a+1: ]):
            if birthdayA == birthdayB:
                return birthdayA

print("""====The Birthday Paradox show us that in a group of N people, the odds
that two of them have marching birthday is surprisingly large.
This program does a Monte Carlo simulatin (that is , repeated random
simulations) to explore this concept.==== """)

MONTHS = ('Jan','Feb','Mar','Apr','May','Jun',
          'Jul','Agu','Sep','Oct','Nov','Dec')

while True:
    print("How many birthday shall I generate?(Max=100)")
    respone = input('> ')
    if respone.isdecimal() and (0< int(respone)<=100):
        numBDays = int(respone)
        break
    
print()
print("Here are ",numBDays, "birthdays:")
birthdays = getBirthday(numBDays)
for i, birthday in enumerate(birthdays):
    if i !=0:
        print(', ',end='')
    monthName = MONTHS[birthday.month -1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

match = getMarch(birthdays)

print('In this simulation, ',end='')
if match != None:
    monthName = MONTHS[birthday.month -1]
    dateText = '{} {}'.format(monthName, match.day)
    print("Multiple people have a birthday on ",dateText )
else:
    print("There are no matching birthdays.")
print()

print("Generating ",numBDays, "random birthdays 100,00 times...")
input('Press Enter to begin...')

print("Let\'s run another 100,00 simulation.")
simMatch = 0
for i in range(100_00):
    if i % 10_000 == 0:
        print(i , "simulations run...")
    birthdays = getBirthday(numBDays)
    if getMarch(birthdays) != None:
        simMatch = simMatch +1
print("100,00 simulation run.")

probabilyty = round(simMatch / 100_00 * 100, 2)
print("Out of 100,000 simulation of ", numBDays, "people, there was a")
print("matching birthday in that group", simMatch , "times. This means")
print("that", numBDays, "people have a", probabilyty, "% change of")
print("having a matching birthday in their group.")
print("That\'s probably more than you would think!")
