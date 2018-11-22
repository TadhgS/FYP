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
        elif (pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBZ' or pos == 'VBZ'):
            verbs.append(word)
        elif (pos == 'RB' or pos == 'RBR' or pos == 'RBS'):
            adverb.append(word)
        else:
            useless.append(word)


print(numpy.random.choice(propernounP) + " " + numpy.random.choice(useless) + " " + numpy.random.choice(verbs))



