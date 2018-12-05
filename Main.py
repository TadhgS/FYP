import nltk
import numpy
import random

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
punt = []

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
        elif (pos == 'SYM'):
            punt.append(word)
        else:
            useless.append(word)
file = open("testfile.txt","w")

for x in range(1,1000):
    x = random.randint(0,8)
    if(x == 1):
        file.write(numpy.random.choice(nouns) + " ")
    elif(x == 2):
        file.write(numpy.random.choice(nounsplural) + " ")
    elif (x == 3):
        file.write(numpy.random.choice(propernounP) + " ")
    elif (x == 4):
        file.write(numpy.random.choice(propernounS) + " ")
    elif (x == 5):
        file.write(numpy.random.choice(verbs) + " ")
    elif (x == 6):
        file.write(numpy.random.choice(verbpast) + " ")
    elif (x == 7):
        file.write(numpy.random.choice(useless) + " ")
    elif (x == 8):
        file.write(numpy.random.choice(useless) + " ")

