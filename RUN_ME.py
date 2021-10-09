from OS_manip import*
from my_library import incorrect_input
from testGUI import do_choice_GUI


create_folder()
clean_start()

action = do_choice_GUI()


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
