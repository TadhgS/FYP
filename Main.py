import nltk
import numpy
import nltk.grammar
import scrapping
from nltk.parse.generate import generate, demo_grammar
from nltk import CFG

scrapping.scrape()

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
adjective = []

grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "Fred" | "Shaggy" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  """)

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
        elif (pos == 'JJ'):
            adjective.append(word)
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


for x in range(1,100):
    '''if (x % 10 == 0):
        file.write("\n")
    y = random.randint(0,5)
    if(y -1 == 5):
        file.write(numpy.random.choice(nouns) + " ")
        y1 = random.randint(0, 2)
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
            y2 = random.randint(0, 2)
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
            y3 = random.randint(0, 2)
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

    file.write(numpy.random.choice(propernounS) + " ")
    file.write(numpy.random.choice(verbs) + " ")
    file.write(numpy.random.choice(nouns) + "")
    file.write(". ")
    file.write("\n")'''

for sentence in generate(grammar1, n=15):
    file.write(' '.join(sentence))
    file.write("\n")
