import nltk
import numpy
import nltk.grammar
import scrapping
from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
from random import randint

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

file = open("testfile.txt","w")

nameOfMonters = ["Old man Jenkins", "Doctor Bob", "Father Browne", "Captain Birdseye"]
monsterList = ["Mummy", "Zombie", "Vampire", "Ghost Pirate"]
location = ["Pyramids", "Mining Town", "Castle", "Beach Town"]
wether = ["Sunny", "Raining", "Thunder and Lightning", "Sunny"]
Treasure = ["Anchient artifacts", "Gold", "Priceless Jewels", "Burried Treasure"]
sentencesTrial = []

##When the team splits up Scooby and Shaggy go together, Velma goes alone and Fred goes with Dalphne
for sentence in sentences:
    for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if(pos == 'NN'):
            nouns.append(word)
            sentencesTrial.append("NN")
        elif (pos == 'NNS'):
            nounsplural.append(word)
            sentencesTrial.append("NNS")
        elif (pos == 'NNP'):
            propernounS.append(word)
            sentencesTrial.append("NNP")
        elif (pos == 'NNPS'):
            propernounP.append(word)
            sentencesTrial.append("NNPS")
        elif (pos == 'JJ'):
            adjective.append(word)
            sentencesTrial.append("JJ")
        elif (pos == 'VB' or  pos == 'VBG' or pos == 'VBN'):
            verbs.append(word)
            sentencesTrial.append("VB")
        elif (pos == 'VBD'):
            verbpast.append(word)
            sentencesTrial.append("VBD")
        elif (pos == 'VBZ' or pos == 'VBP'):
            verb3person.append(word)
            sentencesTrial.append("VBZ")
        elif (pos == 'RB' or pos == 'RBR' or pos == 'RBS'):
            adverb.append(word)
            sentencesTrial.append("RB")
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
                unUsedWords.append(word)
                break
random = randint(0,2)
use = randint(0,4)

monsterUsed = monsterList[use]
locationUsed =  location[use]
nameOfMontersUsed = nameOfMonters[use]
treasureUsed = Treasure[use]
wetherUsed = wether[use]

file.write(monsterUsed + "\n" + locationUsed + "\n" + nameOfMontersUsed + "\n" + treasureUsed + "\n" + wetherUsed + "\n")

'''for x in sentencesTrial:
    if(x == 'NN'):
        if(random == 1):
            file.write(numpy.random.choice(nouns) + " ")
        else:
            file.write(monsterUsed + " ")
    elif(x== 'NNS'):
        file.write(numpy.random.choice(nounsplural) + " ")
    elif(x== 'NNP'):
        file.write(numpy.random.choice(propernounS) + " ")
    elif(x== 'NNPS'):
        file.write(numpy.random.choice(propernounP) + " ")
    elif(x== 'JJ'):
        file.write(numpy.random.choice(verbs) + " ")
    elif(x== 'VB'):
        file.write(numpy.random.choice(adjective)+ " " )
    elif(x=='VBD'):
        file.write(numpy.random.choice(verbpast)+ " ")
    elif(x=='VBZ'):
        file.write(numpy.random.choice(verb3person)+ " ")
    elif(x=='RB'):
        file.write(numpy.random.choice(adverb)+ " ")
    elif(x==','):
        file.write(","+ "\n")
    elif(x=='.'):
        file.write("." + "\n")'''

grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "chased" | "captured"   
  NP -> "Fred" | "Shaggy" | Det N | Det N PP
  Det -> "a"  
  N -> "Ghost" 
  P -> "with" 
""")
grammer1Count =0
for sentence in generate(grammar1, n=10):
    grammer1Count+=1
    if(grammer1Count == 5):
        file.write(' '.join(sentence))
        file.write("\n")

grammar2 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "ate"   
  NP -> "Scooby" | Det N | Det N PP
  Det -> "a"  
  N -> "Scooby Snack"
  P -> "with" 
""")
grammer2Count =0
for sentence in generate(grammar2, n=10):
    grammer2Count+=1
    if(grammer2Count == 2):
        file.write(' '.join(sentence))
        file.write("\n")
