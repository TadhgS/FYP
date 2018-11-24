import nltk
import numpy

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
for x in nouns:
    {
print(numpy.random.choice(nouns) + " " + numpy.random.choice(verbpast) + " " + numpy.random.choice(nounsplural))
    }


