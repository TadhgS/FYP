import scrapping
from tkinter import *
import database
import random

scrapping.scrape()
useableMonsters = []
cluesable = []
characters = []
c1= ""
c2= ""
c3= ""
c4= ""
c5= ""

def write_Story():
    char = database.cursor.execute("SELECT name FROM characters")
    for row in char:
        characters.append(row)
#Done so that all characters will be with characters they are already written with
    c1 = random.choice(characters)
    characters.remove(c1)
    c1 = str(c1)
    c1 = c1.strip("'(),'")

    c2 = random.choice(characters)
    characters.remove(c2)
    c2 = str(c2)
    c2 = c2.strip("'(),'")

    c3 = random.choice(characters)
    characters.remove(c3)
    c3 = str(c3)
    c3 = c3.strip("'(),'")

    c4 = random.choice(characters)
    characters.remove(c4)
    c4 = str(c4)
    c4 = c4.strip("'(),'")

    c5 = random.choice(characters)
    c5 = str(c5)
    c5 = c5.strip("'(),'")

    useLocal = (var.get()).strip("'(),'")

    useAd = []
    adjective = database.cursor.execute("SELECT word FROM words WHERE type ='JJ'")
    for ad in adjective:
        useAd.append(ad)
    adjectiveToUse = random.choice(useAd)
    adjectiveToUse = str(adjectiveToUse)
    adjectiveToUse = adjectiveToUse.strip("'(),'")

    print(c1 + " and " + c2 + " where in the " + adjectiveToUse + " " + useLocal )

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

