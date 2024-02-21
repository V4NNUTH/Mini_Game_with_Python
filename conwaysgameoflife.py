import copy , random , sys , time

#set up the constants
WIDTH = 79 #Width of the cell grid
HEIGHT = 20 # the height of the cell grid

# (!) try changing ALIVE to '#' or another character
ALIVE = 'O' #the character representing a living cell
# (!) Try changing DEAD to '.' or another character
DEAD = ' ' #the character representing a dead cell

nextCells = {}

for x in range(WIDTH):  #loop over every possible column
    for y in range(HEIGHT): #loop over every possible row
        # 50/50 change for starting cells being alive or dead
        if random.randint(0,1) == 0:
            nextCells[(x ,y)] = ALIVE #add a living cell
        else:
            nextCells[(x ,y)] = DEAD #add dead cell
            
while True:
    print("\n" * 50) #separate each step with newlines
    cells = copy.deepcopy(nextCells)
    
    #print cells on the creens
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x ,y)], end='') 
        print()
    print("Press Ctrl-C to quit.")
    
    #calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #get the neighboning coordinates of (x ,y) even if they
            #wrap around the edge:
            left = (x - 1) % WIDTH
            right = (x + 1) %WIDTH
            above = (y -1 ) %HEIGHT
            below = (y + 1) %HEIGHT
            
            #count the number of living neighbors
            numNeighbors = 0
            
            if cells[(left , above)] == ALIVE:
                numNeighbors +=1 # top-left neighbor is alive
            if cells[(x , above)] == ALIVE:
                numNeighbors +=1 # top neighbor is alive
            if cells[(right , above)] == ALIVE:
                numNeighbors +=1 # top-right neighbor is alive
            if cells[(left , y)] == ALIVE:
                numNeighbors +=1 # left neighbor is alive
            if cells[(right , y)] == ALIVE:
                numNeighbors +=1 # right neighbor is alive
            if cells[(left , below)] == ALIVE:
                numNeighbors +=1 # botton-left neighbor is alive
            if cells[(x , below)] == ALIVE:
                numNeighbors +=1 # botton neighbor is alive
            if cells[(right , below)] == ALIVE:
                numNeighbors +=1 # botton-right neighbor is alive
                
            #set cell based in conway's game of life rules
            if cells[(x ,y)] ==ALIVE and (numNeighbors == 2 or numNeighbors ==3):
                #living cells with 2 or3 neighbor stay alive
                nextCells[(x ,y)] = ALIVE
            elif cells[(x ,y)] == DEAD and numNeighbors == 3:
                #dead cells with 3 neighbor become alive
                nextCells[(x ,y)] =ALIVE
            else:
                #everything else dies or stay dead
                nextCells[(x ,y)] = DEAD
                
    try:
        time.sleep(1) 
    except:
        print("Conway's game of life")
        sys.exit()
                