print("Hi")

import datetime


def trial():
    print("Hello world!")
    word = "Hello world!"
    now = datetime.datetime.now()
    print("Current date and time is ")
    d = "Current date and time is "
    print(now.strftime("%A, %d-%m-%Y : %H:%M"))
    t = now.strftime("%A, %d-%m-%Y : %H:%M")
    return word, d, t


def printhello():
    return "Hello_world";


print("Michael")
print("David")
print(trial())
