import nltk
import random

File = open('words.txt')
lines = File.read()
sentences = nltk.sent_tokenize(lines)
nouns = []
verbs = []
adverb = []
useless = []

for sentence in sentences:
    for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if(pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
            nouns.append(word)
        elif (pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBZ' or pos == 'VBZ'):
            verbs.append(word)
        elif (pos == 'RB' or pos == 'RBR' or pos == 'RBS'):
            adverb.append(word)
        else:
            useless.append(word)

sentence_trail = str(nouns[random]) + str(verbs[random]) + str(adverb[random])

print(sentence_trail)

