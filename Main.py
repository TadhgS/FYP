import scrapping
from tkinter import *


#scrapping.scrape()

def write_Story():
    print("Scooby and Shaggy where in the " + str(var.get()))

master = Tk()
master.geometry("300x100")
master.title("Scoody-Doo Story")

Label(master, text="Pick a location for your Story").grid(row=0)

var=StringVar()
var.set("Castle")

choice = OptionMenu(master,var,"Castle","Beach","Ghost Town","Haunted House","Jungle","Carnival","Highway","Pyrimads","Random")

choice.config(font=("Arial",25))
choice.grid(row=1,column=0)

ok = Button(master, text = "OK", command=write_Story )
ok.grid(row=1,column=1)

master.mainloop()

