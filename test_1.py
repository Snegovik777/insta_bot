ask = True

while ask: # this was initialized to True
    message = input('Write your message here: ')
    key = int(input('The encryption key is: '))
    mode = input('Do you want to encrypt or decrypt?')

    # put the coding logic here
    next = input('Do you want to encrypt\\decrypt another message?')
    if next.lower() == 'no':
        ask = False

print('You have finished all messages')