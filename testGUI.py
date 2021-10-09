import tkinter as tk
from tkinter import *


# ------------------------------ FROM RUN_ME MODULE v2 ------------------------------------------
def do_choice_GUI():
    theds = []

    wind = tk.Tk()
    wind.title("CHOOSE TO ENCYPT OR DECRYPT")
    wind.geometry('400x300')
    wind['bg'] = '#26eddd'

    greeting = tk.Label(text='Please select an option below by clicking on the button/box')
    greeting.pack()

    space0 = tk.Label(wind, text='', bg='#26eddd')
    space0.pack()

    def do_abort():
        wind.destroy()

    def do_action_enc():
        wind.destroy()
        theds.append('enc')

    def do_action_dec():
        wind.destroy()
        theds.append('dec')

    Button(
        wind,
        text="PRESS TO ENCRYPT",
        padx=10,
        pady=5,
        command=do_action_enc
        ).pack()

    Button(
        wind,
        text="PRESS TO DECRYPT",
        padx=10,
        pady=5,
        command=do_action_dec
    ).pack()

    Button(
        wind,
        text="PRESS TO CANCEL",
        bg='white',
        fg='black',
        padx=10,
        pady=5,
        command=do_abort
        ).pack()

    wind.mainloop()

    theds = theds[0]#str(theds)
    return theds


# # ------------------------------ FROM RUN_ME MODULE v1 ------------------------------------------
#
# def do_choice_GUI():
#     #content = StringVar()
#     theds = []
#     end_name = ''
#
#
#     wind = tk.Tk()
#     wind.title("CHOOSE TO ENCYPT OR DECRYPT")
#     wind.geometry('400x300')
#     wind['bg'] = '#26eddd'
#
#     greeting = tk.Label(text='Input below...')
#     greeting.pack()
#
#
#
#     def do_abort():
#         wind.destroy()
#
#     def do_action():
#         entry_chars = entry.get()
#         #Label(wind, text= str(entry_chars)+' is registered!', pady=20, bg='#ffbf00').pack()
#         Label(wind, text=str(entry_chars) + ' is registered!', pady=20, bg='#ffbf00').pack()
#         wind.destroy()
#         #theds.append('enc')
#         theds.append(entry_chars)
#
#     # def do_action():
#     #     entry_chars = entry.get()
#     #     #Label(wind, text= str(entry_chars)+' is registered!', pady=20, bg='#ffbf00').pack()
#     #     Label(wind, text=str(entry_chars) + ' is registered!', pady=20, bg='#ffbf00').pack()
#     #     wind.destroy()
#     #     theds.append('dec')
#     #     theds.append(entry_chars)
#
#
#     entry = Entry(wind)
#     entry.pack(pady=10)
#
#     Button(
#         wind,
#         text="PRESS TO ENCRYPT",
#         padx=10,
#         pady=5,
#         command=do_action
#         ).pack()
#
#     Button(
#         wind,
#         text="PRESS TO DECRYPT",
#         padx=10,
#         pady=5,
#         command=do_action
#     ).pack()
#
#     #Button.self.pack(pady=10)
#
#     Button(
#         wind,
#         text="CANCEL",
#         bg='white',
#         fg='black',
#         padx=0,
#         pady=0,
#         command=do_abort
#         ).pack()
#
#
#     wind.mainloop()
#
#     theds = theds[0]#str(theds)
#     return theds








# --------------------------------------- GET PW FROM USER ---------------------------------------------------
def do_pw_GUI():
    theds = []

    wind = tk.Tk()
    wind.title("INPUT YOUR PASSWORD")
    wind.geometry('400x300')
    wind['bg'] = '#26eddd'

    greeting = tk.Label(text='Input password below and click "DONE" when finished')
    greeting.pack()

    space0 = tk.Label(wind, text='', bg='#26eddd')
    space0.pack()

    def do_abort():
        wind.destroy()

    def do_action():
        entry_chars = entry.get()
        wind.destroy()
        theds.append(entry_chars)

    entry = Entry(wind)
    entry.pack(pady=10)

    Button(
        wind,
        text="DONE",
        padx=10,
        pady=5,
        command=do_action
    ).pack()

    Button(
        wind,
        text="CANCEL",
        bg='white',
        fg='black',
        padx=10,
        pady=5,
        command=do_abort
    ).pack()

    wind.mainloop()

    theds = theds[0]
    return theds







from my_library import var

# ------------------------------ FIRST TIME USE AND CREATION ------------------------------------------
def first_GUI():
    wind = tk.Tk()
    wind.title("WELCOME!")
    wind.geometry('800x700')
    wind['bg'] = '#26eddd'

    greeting0 = tk.Label(
        text='Welcome to SafeNotes',
        font=("Helvetica", 26)
        )
    greeting0.pack()

    space0 = tk.Label(wind, text='', bg='#26eddd')
    space0.pack()

    greeting1 = tk.Label(
        width=700,
        text=var,
        bg='#26eddd',
        font=("Helvetica", 14)
    )
    greeting1.pack()

    def do_abort():
        wind.destroy()

    Button(
        wind,
        text="DONE",
        bg='white',
        fg='black',
        padx=10,
        pady=5,
        command=do_abort
        ).pack()

    wind.mainloop()

