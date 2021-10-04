import os
import subprocess
from make_enc import*


# ----- GATHERING PATH INFO -----
output = subprocess.getoutput( 'cd' )
full_path = '' + output


# ----- GETTING USERNAME -----
LHS_start = output.find('Users') + len('Users') + 1
user = output[LHS_start:]
RHS_end = user.find('\\')
user = user[:RHS_end]


# ----- GETTING PRE-USERNAME ------
n = full_path.find(user + '\\')
pre_user = full_path[:n]



# ----- BASIC DIR EST ON DESKTOP ------
target = pre_user + user + '\\Desktop'
target = os.path.join( target, 'SecureData' )



# ----------- CREATING OS PATHS -----------

notes = 'NOTES.txt'
idk = 'secretNOTES.txt'

to_NOTES = os.path.join(target, notes)
to_IDK = os.path.join(target, idk)




def create_folder():
    if( os.path.exists(target)==False ):
        os.mkdir(target)


def create_notes():
    if( os.path.exists(to_NOTES)==False ):
        f = open(to_NOTES, 'a+', encoding='utf_8')
        f.close()


def create_safe_note():
    if( os.path.exists(to_IDK)==False ):
        f = open(to_IDK, 'a+', encoding='utf_8')
        f.close()


def clean_start():
    if( os.path.exists(to_IDK)==False and os.path.exists(to_NOTES)==False ):
        create_notes()
        print('See Desktop -> SecureData -> NOTES')
        print('Re-run this program once you would like to encrypt/decrypt')
        exit()



# ------------------ ENCRYPT ... to_NOTES -> ... ------------------
def do_encrypt():
    f = open(to_NOTES, 'r', encoding='utf_8')
    fi = open(to_IDK, 'a+', encoding='utf_8')
    for i in f:
        fi.write( enc_motor(i) )
    fi.close()
    f.close()
    os.remove(to_NOTES)



# ------------------ DE-CRYPT ... -> to_NOTES ------------------
def do_decrypt():
    f = open(to_IDK, 'r', encoding='utf_8')
    fi = open(to_NOTES, 'a+', encoding='utf_8')
    for i in f:
        fi.write( dec_motor(i) )
    fi.close()
    f.close()
    os.remove(to_IDK)
