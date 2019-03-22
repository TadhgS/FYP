import scrapping
from tkinter import *
import database
import random

scrapping.scrape()
useableMonsters = []

def write_Story():
    cm = 0
    print(var.get())
    print("Scooby and Shaggy where in the " + var.get())
    useable = database.cursor.execute("SELECT monster FROM monsters WHERE local ='" + var.get() +"'")
    for row in useable:
        useableMonsters[cm] = row
        cm+=1
    x = len(useableMonsters)
    i = random.randint[1,x]
    print("There was a" +useableMonsters[i])

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

#"Castle","Beach","Ghost Town","Haunted House","Jungle","Carnival","Highway","Pyramids","Random"