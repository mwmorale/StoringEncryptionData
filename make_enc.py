import random
from my_library import bank
from my_library import odd_chars


def enc_motor(s):
    s = s.lower()
    lst = []
    wrd = ''
    for i in s:
        if( i in bank ):
            ind = bank.index(i)
            if( ind<35 ):
                i = bank[ind+1]
                wrd = wrd+i
                lst.append(i)
            else:
                i = bank[0]
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




def dec_motor(d):
    d = d.lower()
    lst = []
    wrd = ''
    for i in d:
        if( i in bank ):
            ind = bank.index(i)
            if( ind==0 ):
                i = bank[ len(bank)-1 ]
                wrd = wrd+i
                lst.append(i)
            else:
                i = bank[ind - 1]
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
