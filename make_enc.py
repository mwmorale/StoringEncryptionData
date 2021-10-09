import random
from my_library import bank
from my_library import odd_chars
from testGUI import do_pw_GUI


PW = do_pw_GUI()
PW_OFFSET = len(PW)

def enc_motor(s):
    s = s.lower()
    lst = []
    wrd = ''
    for i in s:
        if( i in bank ):
            ind = bank.index(i)
            # rand = ind + len( PW_OFFSET )
            if( ind+PW_OFFSET < len(bank) ): #if rand<35 thennn i=bank[ ind+len(PW_OFFSET) ]
                i = bank[ind+PW_OFFSET]
                wrd = wrd+i
                lst.append(i)
            else:
                i = bank[ ind+PW_OFFSET-len(bank) ] #
                wrd = wrd + i
                lst.append(i)
        elif( i==' ' ):
            i = random.choice(odd_chars)
            wrd = wrd + i
            lst.append(i)
        else:
            wrd = wrd + i
            #lst.append(i)

    return wrd





# ---------- ORIG THAT STILL WORKS WITH STATIC RHS +1 SHIFT -----------
# def enc_motor(s):
#     s = s.lower()
#     lst = []
#     wrd = ''
#     for i in s:
#         if( i in bank ):
#             ind = bank.index(i)
#             # rand = ind + len( PW_OFFSET )
#             if( ind<35 ): #if rand<35 thennn i=bank[ ind+len(PW_OFFSET) ]
#                 i = bank[ind+1]
#                 wrd = wrd+i
#                 lst.append(i)
#             else:
#                 i = bank[0] #
#                 wrd = wrd + i
#                 lst.append(i)
#         elif( i==' ' ):
#             i = random.choice(odd_chars)
#             wrd = wrd + i
#             lst.append(i)
#         else:
#             wrd = wrd + i
#             #lst.append(i)
#
#     return wrd










def dec_motor(d):
    d = d.lower()
    lst = []
    wrd = ''
    for i in d:
        if( i in bank ):
            ind = bank.index(i)
            if( ind-PW_OFFSET < 0 ):
                i = bank[ len(bank) + (ind-PW_OFFSET) ]
                wrd = wrd+i
                lst.append(i)
            else:
                i = bank[ind - PW_OFFSET]
                wrd = wrd + i
                lst.append(i)
        elif( i in odd_chars ):
            i = ' '
            wrd = wrd + i
            lst.append(i)
        else:
            wrd = wrd + i
            #lst.append(i)

    return wrd






# -------------- ORIG THAT WORKS WITH ORIG ENC ------------------
# def dec_motor(d):
#     d = d.lower()
#     lst = []
#     wrd = ''
#     for i in d:
#         if( i in bank ):
#             ind = bank.index(i)
#             if( ind==0 ):
#                 i = bank[ len(bank)-1 ]
#                 wrd = wrd+i
#                 lst.append(i)
#             else:
#                 i = bank[ind - 1]
#                 wrd = wrd + i
#                 lst.append(i)
#         elif( i in odd_chars ):
#             i = ' '
#             wrd = wrd + i
#             lst.append(i)
#         else:
#             wrd = wrd + i
#             #lst.append(i)
#
#     return wrd
