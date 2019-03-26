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

    action = random.choice(verbPull)
    action = str(action)
    action = action.strip("'(),'")

    verb11 = random.choice(verbPull)
    verb11 = str(verb11)
    verb11 = verb11.strip("'(),'")

    verb2 = random.choice(verbPull)
    verb2 = str(verb2)
    verb2 = verb2.strip("'(),'")

    verb3 = random.choice(verbPull)
    verb3 = str(verb3)
    verb3 = verb3.strip("'(),'")

    verb4 = random.choice(verbPull)
    verb4 = str(verb4)
    verb4 = verb4.strip("'(),'")

    verb5 = random.choice(verbPull)
    verb5 = str(verb5)
    verb5 = verb5.strip("'(),'")

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

    adjectiveToUse2 = random.choice(useAd1)
    adjectiveToUse2 = str(adjectiveToUse2)
    adjectiveToUse2 = adjectiveToUse2.strip("'(),'")

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

    fredClue = []
    fredPhrase = database.cursor.execute("SELECT catchphrase FROM characters WHERE name = 'Fred'")
    for x in fredPhrase:
        fredClue.append(x)
    fredCatchPhrase = random.choice(fredClue)
    fredCatchPhrase = str(fredCatchPhrase)
    fredCatchPhrase = fredCatchPhrase.strip("'(),'")

    nounsGroup = []
    nounsGroupBase = database.cursor.execute("SELECT word FROM words WHERE type = 'NN' AND freq >= '5'")
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

    wetherUse = []
    wetherChoice = database.cursor.execute("SELECT wether FROM location WHERE local = '"+ useLocal+"'")
    for w in wetherChoice:
        wetherUse.append(w)
    wether = random.choice(wetherUse)
    wether = str(wether)
    wether = wether.strip("'(),'")

    #fileName = useLocal+i+c1
    #file = open(fileName + ".txt","w")

    print(c1 + " and " + c2 + " where at the " + adjectiveToUse + " " + useLocal)
    print(c3 + ", " + c4 + " and " + c5 + " " + verb1 + " a " + useLocal)
    print("It was " + wether)
    print(c1 + " and " + c2 + " met up with " + c3 + ", " + c4 + " and " + c5)
    print("The gang met " + monsterName)
    print(monsterName + " told stories of a " + adjectiveToUse1 + " " + i)
    print(shaggyCatchPhrase + " " + verb3 + " Shaggy")
    if(c1 != 'Shaggy'):
        print(catchphrase + " " + verb11 + " " + c1)
    if(c1 != 'Fred'):
        print(fredCatchPhrase + " said Fred")
    print(c1 + " and " + c2 + " went to " + nouns + " " + c3 + " " + verb2 + " and " + c4 + " and " + c5 + " went to " + monsterName + "s house")
    print(c4 + " and " + c5 + " found a " + clue + " on the table in " + monsterName + "s house.")
    print("The " + i + " " + action + "ed " + c1 + ", " + c2 + " and " + c3)
    print("Velma " + verb4)
    print(velmaCatchPhrase + " said Velma")
    print(monsterName + " handed Velma her " + adjectiveToUse2 + " glasses")
    print("Stop Them! " + verb5 + " "+ c3)
    print(monsterName + " ran away")
    print("The " + i + " appeared")
    print(c1 + " " + c5 + " ran into the " + i)
    print(c3 + " unmasked the " + i)
    print(monsterName +" gasped the gang")
    print("And I would have got away with it to! If it weren't for you meddling kids! said "+ monsterName)
    print("THE END")



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

