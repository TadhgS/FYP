import nltk
import numpy
import random
import scrapping

scrapeData = scrapping()
scrapeData()

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
            useless.append(word)

file = open("testfile.txt","w")

for x in range(1,50):
    if (x % 7 == 0):
        file.write("\n")
    y = random.randint(0,9)
    if(y -1 == 7):
        file.write(numpy.random.choice(nouns) + " ")
    if(y-1 == 1 or y-1 == 2 or y-1 ==3 or y-1 ==4):
        y = random.randint(1,2)
        if (y == 1):
            file.write(numpy.random.choice(verbs) + " ")
        elif (y == 2):
            file.write(numpy.random.choice(verbpast) + " ")
    if(y == 1):
        file.write(numpy.random.choice(nouns) + " ")
    elif(y == 2):
        file.write(numpy.random.choice(nounsplural) + " ")
    elif (y == 3):
        file.write(numpy.random.choice(propernounP) + " ")
    elif (y == 4):
        file.write(numpy.random.choice(propernounS) + " ")
    elif (y == 5):
        file.write(numpy.random.choice(verbs) + " ")
    elif (y == 6):
        file.write(numpy.random.choice(verbpast) + " ")
    elif (y == 7):
        wordUsed = (numpy.random.choice(useless))
        if(wordUsed != " "):
            wordUsed == "."
            file.write(wordUsed)
            file.write("\n")
        else:
            file.write(wordUsed)
            file.write("\n")
