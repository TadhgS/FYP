import nltk
import numpy
import nltk.grammar
import scrapping
from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
from random import randint
import database

File = open('words.txt')
lines = File.read()
sentences = nltk.sent_tokenize(lines)

runs = 1

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
local = ["Castle","Beach","Beach","Ghost Town"]

file = open("testfile.txt","w")
for x in local:
    scrapping.scrape(runs)
    sentencesTrial = []
    count=0
##When the team splits up Scooby and Shaggy go together, Velma goes alone and Fred goes with Dalphne
    for sentence in sentences:
        for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
            if(pos == 'NN'):
                nouns.append(word.lower())
                sentencesTrial.append("NN")
            elif (pos == 'NNS'):
                nounsplural.append(word.lower())
                sentencesTrial.append("NNS")
            elif (pos == 'NNP'):
                propernounS.append(word.lower())
                sentencesTrial.append("NNP")
            elif (pos == 'NNPS'):
                propernounP.append(word.lower())
                sentencesTrial.append("NNPS")
            elif (pos == 'JJ'):
                adjective.append(word.lower())
                sentencesTrial.append("JJ")
            elif (pos == 'VB' or  pos == 'VBG' or pos == 'VBN'):
                verbs.append(word.lower())
                sentencesTrial.append("VB")
            elif (pos == 'VBD'):
                verbpast.append(word.lower())
                sentencesTrial.append("VBD")
            elif (pos == 'VBZ' or pos == 'VBP'):
                verb3person.append(word.lower())
                sentencesTrial.append("VBZ")
            elif (pos == 'RB' or pos == 'RBR' or pos == 'RBS'):
                adverb.append(word)
                sentencesTrial.append("RB".lower())
            else:
                if(word == ","):
                    useless.append(word)
                    sentencesTrial.append(",")
                    break
                elif(word == "."):
                    useless.append(word)
                    sentencesTrial.append(".")
                    break
                else:
                    unUsedWords.append(word.lower())
                    break
            count+=1

    nounCount = []
    trueNouns = []

    for x in nouns:
        if x in trueNouns:
            a = trueNouns.index(x)
            nounCount[a] +=1
        else:
            trueNouns.append(x)
            a = trueNouns.index(x)
            nounCount.append(1)

    for x in trueNouns:
        i = trueNouns.index(x)
        database.cursor.execute("INSERT INTO words VALUES (?, ?, ?, ?)", (x,'NN',local[runs],nounCount[i]))

    database.cursor.execute("SELECT * FROM words")
    print(database.cursor.fetchall())
runs +=1




