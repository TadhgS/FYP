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

    verbPull = []
    verb1pull = database.cursor.execute("SELECT word FROM words WHERE type ='VBD'")
    for x in verb1pull:
        verbPull.append(x)
    verb1 = random.choice(verbPull)
    verb1 = str(verb1)
    verb1 = verb1.strip("'(),'")

    useable = database.cursor.execute("SELECT monster FROM monsters WHERE local ='" + useLocal +"'")
    for row in useable:
        useableMonsters.append(row)
    i = random.choice(useableMonsters)
    i = str(i)
    i = i.strip("'(),'")

    useAd1 = []
    adjective1 = database.cursor.execute("SELECT word FROM words WHERE type ='JJ' AND local ='" + useLocal + "'")
    for ad in adjective1:
        useAd1.append(ad)
    adjectiveToUse1 = random.choice(useAd1)
    adjectiveToUse1 = str(adjectiveToUse1)
    adjectiveToUse1 = adjectiveToUse1.strip("'(),'")

    adjectiveToUse2 = random.choice(useAd)
    adjectiveToUse2 = str(adjectiveToUse2)
    adjectiveToUse2 = adjectiveToUse2.strip("'(),'")

    action = random.choice(useAd)
    action = str(action)
    action = action.strip("'(),'")

    monst = []
    monstPull = database.cursor.execute("SELECT name FROM monsters WHERE monster ='" + i +"'")
    for x in monstPull:
        monst.append(x)
    monsterName = random.choice(monst)
    monsterName = str(monsterName)
    monsterName = monsterName.strip("'(),'")

    theClue = database.cursor.execute("SELECT clue FROM monsters WHERE monster ='" + i + "'")
    for row in theClue:
        cluesable.append(row)
    clue = random.choice(cluesable)
    clue = str(clue)
    clue = clue.strip("'(),'")

    catchphraseGroup = []
    catchphrasePull = database.cursor.execute("SELECT catchphrase FROM characters WHERE name = '" + c1 + "'")
    for x in catchphrasePull:
        catchphraseGroup.append(x)
    catchphrase = random.choice(catchphraseGroup)
    catchphrase = str(catchphrase)
    catchphrase = catchphrase.strip("'(),'")

    verbPull1 = []
    verb1pull1 = database.cursor.execute("SELECT word FROM words WHERE type ='VBD'")
    for x in verb1pull1:
        verbPull1.append(x)
    verb11 = random.choice(verbPull1)
    verb11 = str(verb11)
    verb11 = verb11.strip("'(),'")

    verb2 = random.choice(verbPull)
    verb2 = str(verb2)
    verb2 = verb2.strip("'(),'")

    fredClue = []
    fredPhrase = database.cursor.execute("SELECT catchphrase FROM characters WHERE name = 'Fred'")
    for x in fredPhrase:
        fredClue.append(x)
    fredCatchPhrase = random.choice(fredClue)
    fredCatchPhrase = str(fredCatchPhrase)
    fredCatchPhrase = fredCatchPhrase.strip("'(),'")

    nounsGroup = []
    nounsGroupBase = database.cursor.execute("SELECT word FROM words WHERE type = 'NN'")
    for n in nounsGroupBase:
        nounsGroup.append(n)
    nouns = random.choice(nounsGroup)
    nouns = str(nouns)
    nouns = nouns.strip("'(),'")

    shaggyClue = []
    shaggyPhrase = database.cursor.execute("SELECT catchphrase FROM characters WHERE name = 'Shaggy'")
    for x in shaggyPhrase:
        shaggyClue.append(x)
    shaggyCatchPhrase = random.choice(shaggyClue)
    shaggyCatchPhrase = str(shaggyCatchPhrase)
    shaggyCatchPhrase = shaggyCatchPhrase.strip("'(),'")

    velmaClue = []
    velmaPhrase = database.cursor.execute("SELECT catchphrase FROM characters WHERE name = 'Velma'")
    for x in velmaPhrase:
        velmaClue.append(x)
    velmaCatchPhrase = random.choice(velmaClue)
    velmaCatchPhrase = str(velmaCatchPhrase)
    velmaCatchPhrase = velmaCatchPhrase.strip("'(),'")

    print(c1 + " and " + c2 + " where at the " + adjectiveToUse + " " + useLocal)
    print(c3 + ", " + c4 + " and " + c5 + " " + verb1 + " to a " + useLocal)
    print(c1 + " and " + c2 + " met up with " + c3 + ", " + c4 + " and " + c5)
    print("The gang met " + monsterName)
    print(monsterName + " told stories of a " + adjectiveToUse + " " + i)
    print(shaggyCatchPhrase + " " + adjectiveToUse2 + " Shaggy")
    if(c1 != 'Shaggy'):
        print(catchphrase + " " + verb11 + " " + c1)
    if(c1 != 'Fred'):
        print(fredCatchPhrase + " said Fred")
    print(c1 + " and " + c2 + " went to " + nouns + " " + c3 + " " + verb2 + " and " + c4 + " and " + c5 + " went to " + monsterName + " house")
    print(c4 + " and " + c5 + " found a " + clue + " on the table in " + monsterName + " house.")
    print("The " + i + " " + action + "ed " + c1 + ", " + c2 + " and " + c3)
    print(velmaCatchPhrase + " said Velma")



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

