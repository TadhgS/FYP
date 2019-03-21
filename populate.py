import database
import nltk
def pop(i):
    loc = i
    sentencesTrial = []
    File = open('words.txt')
    lines = File.read()
    sentences = nltk.sent_tokenize(lines)
    locations = ["Castle","Beach","Beach","Ghost Town","Ghost Town","Haunted House","Jungle","Carnival", "Ghost Town", "Highway", "Castle", "Pyrimades","Beach","Beach","Carnival", "Highway", "Castle" ,"Jungle" ]

    for sentence in sentences:
        for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
            if(pos == 'NN'):
                database.nouns.append(word.lower())
                sentencesTrial.append("NN")
            elif (pos == 'NNS'):
                database.nounsplural.append(word.lower())
                sentencesTrial.append("NNS")
            elif (pos == 'NNP'):
                database.propernounS.append(word.lower())
                sentencesTrial.append("NNP")
            elif (pos == 'NNPS'):
                database.propernounP.append(word.lower())
                sentencesTrial.append("NNPS")
            elif (pos == 'JJ'):
                database.adjective.append(word.lower())
                sentencesTrial.append("JJ")
            elif (pos == 'VB' or  pos == 'VBG' or pos == 'VBN'):
                database.verbs.append(word.lower())
                sentencesTrial.append("VB")
            elif (pos == 'VBD'):
                database.verbpast.append(word.lower())
                sentencesTrial.append("VBD")
            elif (pos == 'VBZ' or pos == 'VBP'):
                database.verb3person.append(word.lower())
                sentencesTrial.append("VBZ")
            elif (pos == 'RB' or pos == 'RBR' or pos == 'RBS'):
                database.adverb.append(word)
                sentencesTrial.append("RB".lower())
            else:
                if(word == ","):
                    database.useless.append(word)
                    sentencesTrial.append(",")
                    break
                elif(word == "."):
                    database.useless.append(word)
                    sentencesTrial.append(".")
                    break
                else:
                    database.unUsedWords.append(word.lower())
                    break

    nounCount = []
    trueNouns = []

    for x in database.nouns:
        if x in trueNouns:
            a = trueNouns.index(x)
            nounCount[a] +=1
        else:
            trueNouns.append(x)
            a = trueNouns.index(x)
            nounCount.append(1)

    for x in trueNouns:
        i = trueNouns.index(x)
        database.cursor.execute("INSERT INTO words VALUES (?, ?, ?, ?)", (x,'NN',locations[loc],nounCount[i]))

    nounpCount = []
    trueNounsp = []

    for x in database.nounsplural:
        if x in trueNounsp:
            a = trueNounsp.index(x)
            nounpCount[a] += 1
        else:
            trueNounsp.append(x)
            a = trueNounsp.index(x)
            nounpCount.append(1)

    for x in trueNounsp:
        i = trueNounsp.index(x)
        database.cursor.execute("INSERT INTO words VALUES (?, ?, ?, ?)", (x, 'NNS', locations[loc], nounpCount[i]))

    pnounCount = []
    truepNouns = []

    for x in database.propernounS:
        if x in truepNouns:
            a = truepNouns.index(x)
            pnounCount[a] += 1
        else:
            truepNouns.append(x)
            a = truepNouns.index(x)
            pnounCount.append(1)

    for x in truepNouns:
        i = truepNouns.index(x)
        database.cursor.execute("INSERT INTO words VALUES (?, ?, ?, ?)", (x, 'NNP', locations[loc], pnounCount[i]))

    pnounpCount = []
    truepNounsp = []

    for x in database.propernounP:
        if x in truepNounsp:
            a = truepNounsp.index(x)
            pnounpCount[a] += 1
        else:
            truepNounsp.append(x)
            a = truepNounsp.index(x)
            pnounpCount.append(1)

    for x in truepNounsp:
        i = truepNounsp.index(x)
        database.cursor.execute("INSERT INTO words VALUES (?, ?, ?, ?)", (x, 'NNPS', locations[loc], pnounpCount[i]))

    adjectCount = []
    trueadject = []

    for x in database.adjective:
        if x in trueadject:
            a = trueadject.index(x)
            adjectCount[a] += 1
        else:
            trueadject.append(x)
            a = trueadject.index(x)
            adjectCount.append(1)

    for x in trueadject:
        i = trueadject.index(x)
        database.cursor.execute("INSERT INTO words VALUES (?, ?, ?, ?)", (x, 'JJ', locations[loc], adjectCount[i]))

    verbCount = []
    trueVerb = []

    for x in database.verbs:
        if x in trueVerb:
            a = trueVerb.index(x)
            verbCount[a] += 1
        else:
            trueVerb.append(x)
            a = trueVerb.index(x)
            verbCount.append(1)

    for x in trueVerb:
        i = trueVerb.index(x)
        database.cursor.execute("INSERT INTO words VALUES (?, ?, ?, ?)", (x, 'VB', locations[loc], verbCount[i]))

    verbpCount = []
    trueVerbp = []

    for x in database.verbpast:
        if x in trueVerbp:
            a = trueVerbp.index(x)
            verbpCount[a] += 1
        else:
            trueVerbp.append(x)
            a = trueVerbp.index(x)
            verbpCount.append(1)

    for x in trueVerbp:
        i = trueVerbp.index(x)
        database.cursor.execute("INSERT INTO words VALUES (?, ?, ?, ?)", (x, 'VBD', locations[loc], verbpCount[i]))

    verb3pCount = []
    trueVerb3p = []

    for x in database.verb3person:
        if x in trueVerb3p:
            a = trueVerb3p.index(x)
            verb3pCount[a] += 1
        else:
            trueVerb3p.append(x)
            a = trueVerb3p.index(x)
            verb3pCount.append(1)

    for x in trueVerb3p:
        i = trueVerb3p.index(x)
        database.cursor.execute("INSERT INTO words VALUES (?, ?, ?, ?)", (x, 'VBZ', locations[loc], verb3pCount[i]))

    adverbCount = []
    trueAdverb = []

    for x in database.adverb:
        if x in trueAdverb:
            a = trueAdverb.index(x)
            adverbCount[a] += 1
        else:
            trueAdverb.append(x)
            a = trueAdverb.index(x)
            adverbCount.append(1)

    for x in trueAdverb:
        i = trueAdverb.index(x)
        database.cursor.execute("INSERT INTO words VALUES (?, ?, ?, ?)", (x, 'RB', locations[loc], adverbCount[i]))

    uselessCount = []
    trueUseless = []

    for x in database.useless:
        if x in trueUseless:
            a = trueUseless.index(x)
            uselessCount[a] += 1
        else:
            trueUseless.append(x)
            a = trueUseless.index(x)
            uselessCount.append(1)

    for x in trueUseless:
        i = trueUseless.index(x)
        database.cursor.execute("INSERT INTO words VALUES (?, ?, ?, ?)", (x, 'PU', locations[loc], uselessCount[i]))

    uuWCount = []
    trueuuW = []

    for x in database.unUsedWords:
        if x in trueuuW:
            a = trueuuW.index(x)
            uuWCount[a] += 1
        else:
            trueuuW.append(x)
            a = trueuuW.index(x)
            uuWCount.append(1)

    for x in trueuuW:
        i = trueuuW.index(x)
        database.cursor.execute("INSERT INTO words VALUES (?, ?, ?, ?)", (x, 'US', locations[loc], uuWCount[i]))

    database.cursor.execute("INSERT INTO monsters VALUES ('Knight','Castle','Old Man Jenkins','Picture Next to Armour')")
    database.cursor.execute("INSERT INTO monsters VALUES ('Vampire','Castle','Andrew the Tour Guide','Make Up')")
    database.cursor.execute("INSERT INTO monsters VALUES ('Shadow','Castle','Frank the Janitor','Name Badge')")

    database.cursor.execute("INSERT INTO monsters VALUES ('Ghost Pirate','Beach','Bill the Lifeguard','Costume')")
    database.cursor.execute("INSERT INTO monsters VALUES ('Seaweed Monster','Beach','Old Fisherman Joe','Seaweed at house')")
    database.cursor.execute("INSERT INTO monsters VALUES ('Shark','Beach','The Mayor','Shark fins in office')")

    database.cursor.execute("INSERT INTO monsters VALUES ('Cowboy Ghost','Ghost Town','Jerry the Businessman ','Cowboy hat')")
    database.cursor.execute("INSERT INTO monsters VALUES ('Miner Ghost','Ghost Town','Gold Hunter Phil','Dust on shoes')")
    database.cursor.execute("INSERT INTO monsters VALUES ('Headless Horse Man','Ghost Town','Envirnmentalist Paddy','Owns a horse')")

    database.cursor.execute("INSERT INTO monsters VALUES ('Francinstein','Haunted House','Sir Godfree','Green paint on skin')")
    database.cursor.execute("INSERT INTO monsters VALUES ('Zombie','Haunted House','The Waiter','Make Up')")
    database.cursor.execute("INSERT INTO monsters VALUES ('Ghost','Haunted House','Jimmy','Glow in the dark paint on cloths')")

    database.cursor.execute("INSERT INTO monsters VALUES ('Ape Man','Jungle','Explorer Fred','Monkey Costume')")
    database.cursor.execute("INSERT INTO monsters VALUES ('Animal Ghosts','Jungle','Environmentalist Jennie','Scratch Marks')")
    database.cursor.execute("INSERT INTO monsters VALUES ('Pterodactyl','Jungle','Tour Guide Bill','Book on flight')")

    database.cursor.execute("INSERT INTO monsters VALUES ('Clown Ghost','Carnival','Ring Master','Access to Costumes')")
    database.cursor.execute("INSERT INTO monsters VALUES ('Zombie','Carnival','Blind Knife Thrower','Not Really Blind')")
    database.cursor.execute("INSERT INTO monsters VALUES ('Animals','Carnival','Worlds Strongest Man','Scratch marks ')")

    database.cursor.execute("INSERT INTO monsters VALUES ('Ghost Car','Highway','Old Town Mayor','Same Car in Garage')")
    database.cursor.execute("INSERT INTO monsters VALUES ('White Lady Ghost','Highway','Miss Anderson','White Dress in closet')")
    database.cursor.execute("INSERT INTO monsters VALUES ('Aliens','Highway','Conspiracy Tom','Fake Space ship on campervan')")

    database.cursor.execute("INSERT INTO monsters VALUES ('Mummy','Pyramid','Museum Curator Petterson ','Bandages in House')")
    database.cursor.execute("INSERT INTO monsters VALUES ('Sand Man','Pyramid','Ramesh the Tour Guide','Sand in hair')")
    database.cursor.execute("INSERT INTO monsters VALUES ('Sphynx','Pyramid','Tour Guide Bob','scratch marks')")