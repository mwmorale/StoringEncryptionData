from OS_manip import*
from my_library import incorrect_input



create_folder()
clean_start()

print( "\nYou are about to perform an action to your notes" )
print('---> Enter enc to encrypt\n---> Enter dec to decrypt')
action = input('\nEnter here: ')


if( action=='' or len(action)>3 ):
    print(incorrect_input)
    exit()
else:
    if( action=='enc' ):
        do_encrypt()
        exit()
    if( action=='dec' ):
        do_decrypt()
        exit()
