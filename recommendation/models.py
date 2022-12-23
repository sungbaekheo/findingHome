from django.db import models
from nltk import bigrams, word_tokenize
from konlpy.tag import Okt

# Create your models here.
def userInput_tokenizer(userInput):
    okt = Okt()
    pos_words = okt.pos(userInput, stem=True, norm=True) # 형태소 분석. 단어는 사전형으로 바꿔주기
    words = [word for word, tag in pos_words if tag in ['Noun', 'Adjective', 'Verb','Adverb']]
    return words

def sentence_vectorizer(input_sentence):
    imsi = None
    for i in input_sentence:
        if imsi is None:
            imsi = i
        else:
            imsi += i
    
    return imsi / len(input_sentence)

def make_bigram(tokens):
    bigram = list(bigrams(tokens))
    haha = []
    for i in bigram:
        imsi = i[0] + " " + i[1]
        haha.append(imsi)

    return haha