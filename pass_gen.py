import sys
import string
import datetime
import os
from easygui import *
from random import *

title = "Password Generator"
options_main = ["EZ 2 Read", "Super Secure", "Exit"]
options = ["Save & Open", "Exit"]


def save():
    file = open("saved_pass.txt", "a")
    file.write(str(datetime.datetime.now()))
    file.write("\n" + password + "\n")
    file.close()
    os.startfile("saved_pass.txt")


def ez():
    characters = string.ascii_letters + string.digits
    global password
    password = "".join(choice(characters) for x in range(randint(8, 12)))

    button = buttonbox("Password is: " + password, title=title, choices=options)

    if button == options[0]:
        save()
    else:
        sys.exit()


def secure():
    characters = string.ascii_letters + string.punctuation + string.digits
    global password
    password = "".join(choice(characters) for x in range(randint(12, 16)))

    button = buttonbox("Password is: " + password, title=title, choices=options)

    if button == options[0]:
        save()
    else:
        sys.exit()


button_main = buttonbox("Please choose a password complexity level.", title=title, choices=options_main)

if button_main == options_main[0]:
    ez()
elif button_main == options_main[1]:
    secure()
else:
    sys.exit()

