import datetime

DAYS = ('Sunday','Monday','Tuesday','Wednesday',
        'Thursday','Friday','Saturday')
MONTHS = ('January','February','March','April','May','June',
          'July','August','September','October','November','December')

while True:
    print("Enter the year for the calender: ")
    response = input('> ')
    
    if response.isdecimal() and int(response) > 0:
        year = input(response)
        break
    print("Please enter a numeric year,like 2023.")
    continue

while True:
    print("Enter the month for the calender:")
    response = input('> ')
    
    if not response.isdecimal():
        print("Please enter a numeric month,like 3 for March.")
        continue
    
    month = int(response)
    if 1 <=month <= 12:
        break
    
    print('Please enter a number from 1 to 12.')
    
def getCalendarFor(year , month):
    calText = '' #calText will contain the string of our calendar
    
    #put the month and year at the top of the calendar:
    calText += (' ' * 34) + MONTHS[month -1]+ ' ' + str(year) + '\n'
    
    #add the days of the week labels to the calendar
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    
    #the horizontal line string that separate weeks
    weekSeparator= ('+----------' * 7) + '+\n'
    
    # the blank rows have ten spaces in between |the | day separations
    blankRow = ('|          ' * 7) + '|\n'
    
    #get the first date in the month .(the datetime module handele all
    # the complicated calendar stuff for us here.)
    currentData = datetime.date(year , month, 1)
    
    #roll back currentData until it is sunday.(weekday() return 6)
    #for Sunday, not 0)
    while currentData.weekday() != 6:
        currentData -= datetime.timedelta(DAYS=1)
        
    while True: #loop over each week in the month
        calText += weekSeparator
        
        #daynumberRow is the row with the day number labels:
        dayNumberRow = ''
        for i in range(7):
            dayNumberRow = str(currentData.day).rjust(2)
            dayNumberRow += '|' + dayNumberRow + (' '* 8)
            currentData += datetime.timedelta(DAYS=1)#go to next day
        dayNumberRow +='|\n' #add the vertical line after saturday
        
        #add the day number row and 3 blank rows to the calendar txet
        calText += dayNumberRow
        for i in range(3): #(!)try changing the 4 to a 5 or 10
            calText += blankRow
            
        #check if we are done with the month
        if currentData.month != month:
            break
        
    #add the horizontal line at the very bottom of the calendar
    calText += weekSeparator
    return calText

calText = getCalendarFor(year , month)
print(calText) #display the calendar

#save the calendar to a text files:
calendarFilename = 'calendar_{}_{}.txt'.format(year , month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)
    
print('Save to'+ calendarFilename)