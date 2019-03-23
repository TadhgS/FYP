import scrapping
from tkinter import *
import database
import random

scrapping.scrape()
useableMonsters = []
cluesable = []

def write_Story():
    '''if(var.get() == "('Castle',)"):
        useLocal = "Castle"
    elif(var.get() == "('Beach',)"):
        useLocal = "Beach"
    elif (var.get() == "('Ghost Town',)"):
        useLocal = "Ghost Town"
    elif (var.get() == "('Haunted House',)"):
        useLocal = "Haunted Hause"
    elif (var.get() == "('Jungle',)"):
        useLocal = "Jungle"
    elif (var.get() == "('Carnival',)"):
        useLocal = "Carnival"
    elif (var.get() == "('Highway',)"):
        useLocal = "Highway"
    else:
        useLocal = " "'''''
    useLocal = (var.get()).strip("'(),'")
    #print(var.get())
    print("Scooby and Shaggy where in the " + useLocal )
    useable = database.cursor.execute("SELECT monster FROM monsters WHERE local ='" + useLocal +"'")
    for row in useable:
        useableMonsters.append(row)
    i = random.choice(useableMonsters)
    i = str(i)
    i = i.strip("'(),'")
    print("There was a " + i)
    theClue = database.cursor.execute("SELECT clue FROM monsters WHERE monster ='" + i + "'")
    for row in theClue:
        cluesable.append(row)
    clue = random.choice(cluesable)
    clue = str(clue)
    clue = clue.strip("'(),'")
    print("They found a " + clue + " on the table.")

master = Tk()
master.geometry("300x100")
master.title("Scoody-Doo Story")

Label(master, text="Pick a location for your Story").grid(row=0)

var = StringVar()

choices = database.cursor.execute("SELECT DISTINCT local FROM monsters")

choice = OptionMenu(master, var, *choices)


choice.config(font=("Arial",25))
choice.grid(row=1,column=0)

ok = Button(master, text = "OK", command=write_Story )
ok.grid(row=1,column=1)

master.mainloop()

