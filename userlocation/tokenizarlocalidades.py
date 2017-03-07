
# -*- coding: utf-8 -*

from __future__ import division
import nltk, re, pprint
import codecs
import unicodedata
from nltk.corpus import stopwords
import string
from collections import Counter
import csv


def get_tokens():

   camino = ('localidades.txt')
   line = codecs.open(camino, encoding='utf-8').read()
   una=line
   una=una.lower()
   una=una.encode('unicode_escape')
   no_punctuation = una.translate(None, string.punctuation)
   tokens = nltk.word_tokenize(no_punctuation)
   return tokens

tokens = get_tokens()
#count = Counter(tokens)
#tokens.to_csv('tweetsnegativostokenizados.csv', index=False, encoding='utf-8')
#hola= open('tweetspositivostokenizados.txt','a')
#hola.writelines(tokens)
guardar= open("contadorlocalidades.txt","a")
guardar.write(str(Counter(tokens)))

#print '######'
#print count.most_common(6000)
#print count

print len(tokens)