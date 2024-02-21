from secrets import choice
import sys, random , time

try:
    import bext
except ImportError:
    sys.exit()

WIDTH, HEIGHT = bext.size()
WIDTH -=1

NUMBER_OF_LOGOS = 5 # (!) Try changing this to 1 or 100.
PAUSE_AMOUNT = 0.2 # (!) Try changing this to 1.0 or 0.0.

COLORS = ['red','green','yellow','blue','magenta','cyan','white']
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT  = 'dl'

DIRECTION = (UP_RIGHT, UP_LEFT , DOWN_RIGHT , DOWN_LEFT)

COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()

    logos =[]
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                        X: random.randint(1, WIDTH - 4),
                        Y: random.randint(1, HEIGHT - 4),
                        DIR: random.choice(DIRECTION)})
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -=1

    cornerBounces = 0
    while True:
        for logo in logos:
            bext.goto(logo[X],logo[Y])
            print("   ",end='')

            originalDirection = logo[DIR]

            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces +=1
            elif logo[X] == 0 and logo[Y] == HEIGHT -1:
                logo[DIR] = UP_RIGHT
                cornerBounces +=1
            elif logo[X] == WIDTH -3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces +=1
            elif logo[X] == WIDTH -3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces +=1

            #see if the logo bounces off the left edge
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT
            
            #see if the logo bounces off the right edge
            #(width -3 becouse  DVD has 3 letters)
            elif logo[X] == WIDTH -3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH -3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            #see if the logo bounces off the top edge
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            #see if the logo bounces off the bottom edge
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != originalDirection:
                #change color when the logo bounces
                logo[COLOR] = random.choice(COLORS)

            #Move the logo.(X move by 2 becouse the terminal)
            #character are twice as tall as they are wide
            if logo[DIR] == UP_RIGHT:
                logo[X] +=2
                logo[Y] -=1
            elif logo[DIR] == UP_LEFT:
                logo[X] -=2
                logo[Y] -=1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] +=2
                logo[Y] +=1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -=2
                logo[Y] +=1
        # Display number of corner bounces
        bext.goto(5,0)
        bext.fg('white')
        print("Corner bounces: ",cornerBounces, end='')

        for logo in logos:
            #Draw the logos at their new location
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print("DVD",end='')

        bext.goto(0,0)

        sys.stdout.flush() #required for bext-using programs
        time.sleep(PAUSE_AMOUNT)

#if this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Bounces DVD Logo")
        sys.exit() # when CTRl-C is pressed end the program
            
            
                
                
                



