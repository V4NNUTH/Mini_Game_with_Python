print("Enter the encrypt Ceasar cipher message to hack.")
message = input('> ')

SYMBOLES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLES)): #loop through every possible key.
    translated = ''
    for symbol in message:
        if symbol in SYMBOLES:
            num = SYMBOLES.find(symbol) #get number of the symbol
            num = num - key
            
            #handle the wrap around if num is less than 0
            if num < 0:
                num = num + len(SYMBOLES)
            
            #add decrypt number symbbol in translated
            translated = translated + SYMBOLES[num]
        else:
            #just add the symbol without decrypting 
            translated = translated +symbol
            
    print("Key #{}: {}".format(key, translated))