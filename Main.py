import nltk
import numpy
import random
#import scrapping

#scrapeData = scrapping()
#scrapeData()

File = open('words.txt')
lines = File.read()
sentences = nltk.sent_tokenize(lines)

nouns = []
nounsplural = []
propernounS = []
propernounP = []
verbs = []
verbpast = []
verb3person = []
adverb = []
useless = []
unUsedWords = []

for sentence in sentences:
    for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if(pos == 'NN'):
            nouns.append(word)
        elif (pos == 'NNS'):
            nounsplural.append(word)
        elif (pos == 'NNP'):
            propernounS.append(word)
        elif (pos == 'NNPS'):
            propernounP.append(word)
        elif (pos == 'VB' or  pos == 'VBG' or pos == 'VBN'):
            verbs.append(word)
        elif (pos == 'VBD'):
            verbpast.append(word)
        elif (pos == 'VBZ' or pos == 'VBP'):
            verb3person.append(word)
        elif (pos == 'RB' or pos == 'RBR' or pos == 'RBS'):
            adverb.append(word)
        else:
            if(word == ","):
                useless.append(word)
            elif(word == "."):
                useless.append(word)
            else:
                unUsedWords.append(word)

file = open("testfile.txt","w")

for x in range(1,50):
    if (x % 7 == 0):
        file.write(",")
        file.write("\n")
    y = random.randint(0,6)
    if(y -1 == 5):
        file.write(numpy.random.choice(nouns) + " ")
        y1 = random.randint(0, 6)
        if (y1 == 1):
            file.write(numpy.random.choice(nouns) + " ")
        elif (y1 == 2):
            file.write(numpy.random.choice(nounsplural) + " ")
        elif (y1 == 3):
            file.write(numpy.random.choice(propernounP) + " ")
        elif (y1 == 4):
            file.write(numpy.random.choice(propernounS) + " ")
        elif (y1 == 5):
            file.write(numpy.random.choice(useless))
            file.write("\n")
    if(y-1 == 1 or y-1 == 2 or y-1 ==3 or y-1 ==4):
        y = random.randint(1,2)
        if (y == 1):
            file.write(numpy.random.choice(verbs) + " ")
            y2 = random.randint(0, 6)
            if (y2 == 1):
                file.write(numpy.random.choice(nouns) + " ")
            elif (y2 == 2):
                file.write(numpy.random.choice(nounsplural) + " ")
            elif (y2 == 3):
                file.write(numpy.random.choice(propernounP) + " ")
            elif (y2 == 4):
                file.write(numpy.random.choice(propernounS) + " ")
            elif (y2 == 5):
                file.write(numpy.random.choice(useless))
                file.write("\n")
        elif (y == 2):
            file.write(numpy.random.choice(verbpast) + " ")
            y3 = random.randint(0, 6)
            if (y3 == 1):
                file.write(numpy.random.choice(nouns) + " ")
            elif (y3 == 2):
                file.write(numpy.random.choice(nounsplural) + " ")
            elif (y3 == 3):
                file.write(numpy.random.choice(propernounP) + " ")
            elif (y3 == 4):
                file.write(numpy.random.choice(propernounS) + " ")
            elif (y3 == 5):
                file.write(numpy.random.choice(useless))
                file.write("\n")
    if(y == 1):
        file.write(numpy.random.choice(nouns) + " ")
    elif(y == 2):
        file.write(numpy.random.choice(nounsplural) + " ")
    elif (y == 3):
        file.write(numpy.random.choice(propernounP) + " ")
    elif (y == 4):
        file.write(numpy.random.choice(propernounS) + " ")
    elif (y == 5):
        file.write(numpy.random.choice(useless))
        file.write("\n")
