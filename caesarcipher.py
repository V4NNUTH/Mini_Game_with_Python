
try:
    import pyperclip    #Pyperclip copis text to the clipboard
except ImportError:
    pass #if pyperclip is not intalled, do nothing it is no big deal

#Every possible sybol that can be encrypted decrypted
#you can add numbers and punctuation marks to encrypt those symbol as well

SYMBOLES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    print("Do you want to (e)ncrypt or (d)ecrypt? ")
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print("please enter the e or d.")
    
while True:
    maxKey = len(SYMBOLES) -1
    print("Please Enter the key (0 to {}) to use.".format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <=int(response) < len(SYMBOLES):
        key = int (response)
        break
    
print("Enter the message to {}.".format(mode))
messages = input("> ")
messages = messages.upper()

translated = ''

for symbol in messages:
    if symbol in SYMBOLES:
        num = SYMBOLES.find(symbol) #get the number of the symbol
        if mode =='encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num -key
        
            #handle the wrap around if num is large than the length of symbols or less htan 0
        if num >= len(SYMBOLES):
            num = num - len(SYMBOLES)
        elif num < 0:
            num = num +len(SYMBOLES)
            
        #add encrypt/decrypt number symbol to translate
        translated = translated +SYMBOLES[num]
    else:
        #just add the symbol without encrypy/decrypt
        translated = translated + symbol
        
print(translated)

try:
    pyperclip.copy(translated)
    print("Full {}ed text copied to clipbord.".format(mode))
except:
    pass #do nothing if pyperclip wasn't installed.
    