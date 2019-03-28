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

    master.destroy()
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

    verb6 = random.choice(verbPull)
    verb6 = str(verb6)
    verb6 = verb6.strip("'(),'")

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

    scoobyphraseGroup = []
    scoobyphrasePull = database.cursor.execute("SELECT catchphrase FROM characters WHERE name = 'Scooby Doo'")
    for x in scoobyphrasePull:
        scoobyphraseGroup.append(x)
    scoobyphrase = random.choice(scoobyphraseGroup)
    scoobyphrase = str(scoobyphrase)
    scoobyphrase = scoobyphrase.strip("'(),'")

    fredClue = []
    fredPhrase = database.cursor.execute("SELECT catchphrase FROM characters WHERE name = 'Fred'")
    for x in fredPhrase:
        fredClue.append(x)
    fredCatchPhrase = random.choice(fredClue)
    fredCatchPhrase = str(fredCatchPhrase)
    fredCatchPhrase = fredCatchPhrase.strip("'(),'")

    nounsGroup = []
    nounsGroupBase = database.cursor.execute("SELECT word FROM words WHERE type = 'NNP' AND freq >= '5'")
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

    file = open("textfile.txt","w")

    #Randomise sentences ?

    file.write("Scooby Doo and the " + adjectiveToUse1 + " " + i + "\n")
    file.write("\n")
    file.write(c1 + " and " + c2 + " were at the " + adjectiveToUse + " " + useLocal + "\n")
    file.write(c3 + ", " + c4 + " and " + c5 + " " + verb1 + " to the " + useLocal+ "\n")
    file.write("It was " + wether+ "\n")
    file.write(c1 + " and " + c2 + " met up with " + c3 + ", " + c4 + " and " + c5+ "\n")
    file.write("The gang met " + monsterName+ "\n")
    file.write(monsterName + " told stories of a " + adjectiveToUse1 + " " + i+ "\n")
    if(c1 != 'Shaggy'):
        file.write(catchphrase + " " + verb11 + " " + c1+ "\n")
    if(c1 == 'Velma'):
        file.write("Jinkies " + verb11 + " " + c1 + "\n")
    if(c1 == 'Scooby Doo'):
        file.write("Rut Ro wimpered " + c1)
    if(c1 != 'Fred'):
        file.write(fredCatchPhrase + " said Fred"+ "\n")
    if(c1 == 'Shaggy'):
        if(c2 == 'Scooby Doo'):
            file.write(c1 + " and " + c2 + " went to the " + nouns + " " + c3 + " " + verb2 + " and " + c4 + " and " + c5 + " went to " + monsterName + "s house"+ "\n")
        elif(c3 == 'Scooby Doo'):
            file.write(c1 + " and " + c3 + " went to the " + nouns + " " + c2 + " " + verb2 + " and " + c4 + " and " + c5 + " went to " + monsterName + "s house"+ "\n")
        elif (c4 == 'Scooby Doo'):
            file.write(c1 + " and " + c4 + " went to the " + nouns + " " + c3 + " " + verb2 + " and " + c2 + " and " + c5 + " went to " + monsterName + "s house" + "\n")
        elif (c5 == 'Scooby Doo'):
            file.write(c1 + " and " + c5 + " went to the " + nouns + " " + c3 + " " + verb2 + " and " + c4 + " and " + c2 + " went to " + monsterName + "s house" + "\n")
    elif (c2 == 'Shaggy'):
        if (c1 == 'Scooby Doo'):
            file.write(c1 + " and " + c2 + " went to the " + nouns + " " + c3 + " " + verb2 + " and " + c4 + " and " + c5 + " went to " + monsterName + "s house" + "\n")
        elif (c3 == 'Scooby Doo'):
            file.write(c2 + " and " + c3 + " went to the " + nouns + " " + c1 + " " + verb2 + " and " + c4 + " and " + c5 + " went to " + monsterName + "s house" + "\n")
        elif (c4 == 'Scooby Doo'):
            file.write(c2 + " and " + c4 + " went to the " + nouns + " " + c3 + " " + verb2 + " and " + c1 + " and " + c5 + " went to " + monsterName + "s house" + "\n")
        elif (c5 == 'Scooby Doo'):
            file.write(c2 + " and " + c5 + " went to the " + nouns + " " + c3 + " " + verb2 + " and " + c4 + " and " + c1 + " went to " + monsterName + "s house" + "\n")
    else:
        file.write(c1 + " and " + c2 + " went to the " + nouns + " " + c3 + " " + verb2 + " and " + c4 + " and " + c5 + " went to " + monsterName + "s house" + "\n")
    file.write(c4 + " and " + c5 + " found a " + clue + " on the table in " + monsterName + "s house."+ "\n")
    file.write("The " + i + " " + action + " " + c1 + ", " + c2 + " and " + c3+ "\n")
    file.write("Velma " + verb4+ "\n")
    file.write(velmaCatchPhrase + " said Velma"+ "\n")
    file.write(monsterName + " handed Velma her " + adjectiveToUse2 + " glasses"+ "\n")
    file.write("Stop! " + verb5 + " "+ c3+ "\n")

    #60 get aways .....
    if(i == 'Knight'):
        if(wether == 'Stormy'):
            file.write("Lightning " + verb6 + " distracting the gang")
            file.write(monsterName + " ran into a hidden passage.\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " ran into the " + i + "\n")
        elif(wether == 'Raining'):
            file.write(monsterName + " splashed water in at the gang and ran away\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " ran into the " + i + "\n")
        elif(wether == 'Misty'):
            file.write(monsterName + " backed into the mist\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " ran out of the mist into the " + i + "\n")
        else:#Dark
            file.write(monsterName + " backed into a dark corner\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " ran out of the dark and into the " + i + "\n")
    elif(i == 'Vampire'):
        if (wether == 'Stormy'):
            file.write(monsterName + " used the flashes of lightning to run away\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " ran into the " + i + " and tackled it.\n")
        elif (wether == 'Raining'):
            file.write(monsterName + " jumped into the rain\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " jumped after the " + i + " and landed on them\n")
        elif (wether == 'Misty'):
            file.write(monsterName + " backed into the mist\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " used the mist to surprise the " + i + " and knock him over\n")
        else:#Dark
            file.write(monsterName + " backed into a dark corner\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " ran into the dark and bumped into the " + i + "\n")
    elif (i == 'Shadow'):
        if (wether == 'Stormy'):
            file.write(monsterName + " disappeared after a lightning flash \n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " tripped the " + i + "\n")
        elif (wether == 'Raining'):
            file.write(monsterName + " jumped into a trap door\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " shined a flash light at the " + i + " blinding it.\n")
        elif (wether == 'Misty'):
            file.write(monsterName + " disappeared into the " + wether + "surrounding\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " tied up the " + i + "\n")
        else:#Dark
            file.write(monsterName + " back into the darkness\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " trapped the " + i + "\n")


    elif (i == 'Ghost Pirate'):
        if (wether == 'Sunny'):
            file.write(monsterName + " sailed away\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " sailed out to the " + i + " and tied it up\n")
        else:#Misty
            file.write(monsterName + " sailed into the mist\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " threw a fishing net at the " + i + "\n")
    elif (i == 'Seaweed Monster'):
        if (wether == 'Sunny'):
            file.write(monsterName + " backed into the sea\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " trapped the " + i + " in quick sand\n")
        else:#Misty
            file.write(monsterName + " disappeared into the " + wether +" water\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " poured water from the peer on the " + i + "\n")
    elif (i == 'Shark'):
        if (wether == 'Sunny'):
            file.write(monsterName + " ran into the sea\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " shot a harpoon at the " + i + "s fin\n")
        else:#Misty
            file.write(monsterName + " jumped from the peer into the water\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " tricked the " + i + " to go onto the land\n")


    elif (i == 'Cowboy Ghost'):
        if (wether == 'Cloudy'):
            file.write(monsterName + " rode there horse away\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " tripped the horse " + i + "\n")
        else:#Foggy
            file.write(monsterName + " used the fog to disappear\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " laseoed the " + i + "\n")
    elif (i == 'Miner Ghost'):
        if (wether == 'Cloudy'):
            file.write(monsterName + " ran into the mine\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " hit the " + i + " with a minecart\n")
        else:#Foggy
            file.write(monsterName + " ran into the police station in the " + useLocal + "\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " trapped the " + i + " in a barrel\n")
    elif (i == 'Headless Horse Man'):
        if (wether == 'Cloudy'):
            file.write(monsterName + " jumped on his horse and rode away\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " knocked over the water tower, knocking the " + i + " off there horse\n")
        else:#Foggy
            file.write(monsterName + " ran into the fog\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " lead the " + i + " to a hole in the ground\n")


    elif (i == 'Francinstein'):
        if (wether == 'Stormy'):
            file.write(monsterName + " ran up the stairs\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " dropped a chandelier on the " + i + "\n")
        else:#Misty
            file.write(monsterName + " ran into the " + wether + " garden\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(i + " fell into an open grave\n")
    elif (i == 'Zombie'):
        if(useLocal == 'Haunted House'):
            if (wether == 'Stormy'):
                file.write(monsterName + " ran through a secret passage\n")
                file.write("The " + i + " appeared" + "\n")
                file.write(c1 + " and " + c5 + " tripped the " + i + " down the stairs\n")
            else:#Misty
                file.write(monsterName + " ran into the nearby graveyard\n")
                file.write("The " + i + " appeared" + "\n")
                file.write(c1 + " and " + c5 + " fell down the stairs and onto the " + i + "\n")
        else:#Carnival
            if (wether == 'Dark'):
                file.write(monsterName + " ran into the house of mirrors\n")
                file.write("The " + i + " appeared" + "\n")
                file.write(c1 + " and " + c5 + " shot " +c4+" out of a cannon at the " + i + "\n")
            elif (wether == 'Cloudy'):
                file.write(monsterName + " disappeared into the circus tent\n")
                file.write("The " + i + " appeared" + "\n")
                file.write(c1 + " and " + c5 + " tied up the " + i + " with tightrope wire\n")
            else:  # Overcast
                file.write(monsterName + " threw a knife at the lights and ran away\n")
                file.write("The " + i + " appeared" + "\n")
                file.write(c1 + " and " + c5 + " threw water baloons at the " + i + "\n")
    elif (i == 'Ghost'):
        if (wether == 'Stormy'):
            file.write(monsterName + " ran behind a fake wall\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " pushed the " + i + " down the stairs\n")
        else:#Misty
            file.write(monsterName + " ran into the "+ wether+" garden\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " ran into the garden and knocked the " + i + " over\n")


    elif (i == 'Ape Man'):
        if (wether == 'Sunny'):
            file.write(monsterName + " climbed into a tree house\n")
            file.write("The " + i + " jumped down" + "\n")
            file.write(c1 + " and " + c5 + " tied up the " + i + " with vines\n")
        else:#Raining
            file.write(monsterName + " ran out of the shelter\n")
            file.write("The " + i + " appeared in the trees" + "\n")
            file.write(c1 + " and " + c5 + " shot the " + i + " with a tranquilizer bullet\n")
    elif (i == 'Aminal Ghosts'):
        if (wether == 'Sunny'):
            file.write(monsterName + " ran deep into the "+useLocal+"\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " set an animal trap for the " + i + "\n")
        else:#Raining
            file.write(monsterName + " ran into the rain\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " tricked the " + i + " into running into quick sand\n")
    elif (i == 'Pterodactyl'):
        if (wether == 'Sunny'):
            file.write(monsterName + " climbed a tree\n")
            file.write("The " + i + " appeared from above" + "\n")
            file.write(c1 + " and " + c5 + " lassoed the " + i + "s leg and pulled it out of the air\n")
        else:#Raining
            file.write(monsterName + " climbed a tree\n")
            file.write("The " + i + " appeared out of the rain" + "\n")
            file.write(c1 + " and " + c5 + " shot the " + i + " with a tranquilizer dart\n")


    elif (i == 'Clown Ghost'):
        if (wether == 'Dark'):
            file.write(monsterName + " ran into the haunted house\n")
            file.write("The " + i + " appeared out of the dark" + "\n")
            file.write(i + " ran out of the haunted house screaming and fell over\n")
        elif (wether == 'Cloudy'):
            file.write(monsterName + " ran to there trailer\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(i + " was grabbed by the worlds strongest man\n")
        else:#Overcast
            file.write(monsterName + " ran into the clown tent\n")
            file.write("The " + i + " walked out of the clown tent" + "\n")
            file.write(c1 + " and " + c5 + " hot the " + i + " with a tiny clown car\n")
    elif (i == 'Aminals'):
        if (wether == 'Dark'):
            file.write(monsterName + " disappeared without a trace\n")
            file.write("The " + i + " surrounded the gang" + "\n")
            file.write(c1 + " and " + c5 + " fed the animals and "+ c3 + " cought " + i + "\n")
        elif (wether == 'Cloudy'):
            file.write(monsterName + " ran to the petting zoo\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " trapped the " + i + " in the animal pen\n")
        else:#Overcast
            file.write(monsterName + " pushed passed the gang\n")
            file.write("The " + i + " appeared" + "\n")
            file.write("Scooby talked to the " + i + " and they didnt attack \n")


    elif (i == 'Ghost Car'):
        if (wether == 'Sunny'):
            file.write(monsterName + " got in there car and drove away\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " shot the cars tires and the " + i + " stopped\n")
        else:#Raining
            file.write(monsterName + " dove away\n")
            file.write("The " + i + " appeared" + "\n")
            file.write("The " + i + " skidded in the rain and crashed\n")
    elif (i == 'White Lady Ghost'):
        if (wether == 'Sunny'):
            file.write(monsterName + " ran into there car\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " tied the " + i + " up\n")
        else:#Raining
            file.write(monsterName + " ran out of the rain\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(i + "s make up started running in the rain\n")
    elif (i == 'Aliens'):
        if (wether == 'Sunny'):
            file.write(monsterName + " ran to there RV\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " used a mirror to blind the " + i + "\n")
        else:#Raining
            file.write(monsterName + " ran to there RV\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " tackled the " + i + "\n")


    elif (i == 'Mummy'):
        if (wether == 'Overcast'):
            file.write(monsterName + " ran into the pyramid\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " unraveled the " + i + "\n")
        elif (wether == 'Sunny'):
            file.write(monsterName + " ran into the dessert\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " set the " + i + " on fire using a mirror\n")
        else:#Raining
            file.write(monsterName + " ran into great pyramid\n")
            file.write("The " + i + " appeared" + "\n")
            file.write("The " + i + "s rags began to fall off\n")
    elif(i == 'Sand Man'):
        if (wether == 'Overcast'):
            file.write(monsterName + " ran into a secret passage in the sand\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " used the mystery machine to knock over the " + i + "\n")
        elif (wether == 'Sunny'):
            file.write(monsterName + " ran away into the dessert\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " sprayed the " + i + " with water, melting it\n")
        else:#Raining
            file.write(monsterName + " ran out of the rain into the pyramid\n")
            file.write("The " + i + " appeared" + "\n")
            file.write("The " + i + " melted in the rain\n")
    else:
        if (wether == 'Overcast'):
            file.write(monsterName + " ran up to the "+ i +"\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " shot the " + i + " with a tranquilizer dart\n")
        elif (wether == 'Sunny'):
            file.write(monsterName + " ran into a pyramid\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " trapped the " + i + " in a hole\n")
        else:#Raining
            file.write(monsterName + " ran into a secret passage in the sand\n")
            file.write("The " + i + " appeared" + "\n")
            file.write(c1 + " and " + c5 + " lassoed the " + i + "s legs\n")


    file.write(c3 + " unmasked the " + i+ "\n")
    file.write("'" + monsterName + "'" +" gasped the gang"+ "\n")
    file.write("And I would have got away with it to! If it weren't for you meddling kids! and your dumb Dog! said "+ monsterName+ "\n")
    file.write(scoobyphrase + " laughed Scooby \n")
    file.write("THE END"+ "\n")


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
