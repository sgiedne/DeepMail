import os
import pandas as pd
import nltk
import gensim
from gensim import corpora, models, similarities
import json
import unicodedata

def read_json_data(filename):
    sentences = []
    with open(filename) as json_data:
        for line in json_data:
            article = {}
            article = json.loads(line)
            title = nltk.word_tokenize(unicodedata.normalize('NFKD', article['title']).encode('ascii','ignore'))
            text = nltk.word_tokenize(unicodedata.normalize('NFKD', article['text']).encode('ascii','ignore'))
            sentences.append(title)
            sentences.append(text)
    save_parsed_data(sentences)


def train_model(sentences):
    model = gensim.models.Word2Vec(sentences, size = 200, workers=4)
    model.save('testmodel')

def load_model():
    model = gensim.models.Word2Vec.load('testmodel')
    return model

def save_parsed_data(sentences):
    parsed_json = open('parsed_json.txt', 'w')
    for item in sentences:
        parsed_json.write("%s\n" % item)

def read_parsed_data():
    sentences = []
    with open('parsed_json.txt') as data:
        for line in data:
            sentences.append(line)
    return sentences



def get_similar(input,model):
    return model.wv.most_similar(input, topn=10)

def isXinY(x,y):
    res = True
    for i in x:
        if i in y:
            continue
        else:
            res = False
            break
    return res




def get_mails(input,sentences):
    model = load_model()
    list_depth0 = get_similar(input,model)

    search_result = []

    for x in range(0,3):
        search_result.append(input + [list_depth0[x][0]]) #(1,2)
        list_depth1 = get_similar(input + [list_depth0[x][0]],model) 
        search_result.append([list_depth0[x][0], list_depth1[x][0]]) #(2,5)
        search_result.append(input + [list_depth1[x][0]]) #(1,5)
        search_result.append(input + [list_depth0[x][0], list_depth1[x][0]]) #(1,2,5)


    for x in search_result:
        print x

    res = set()


    for x in search_result:
        for y in sentences:
            if isXinY(x,y):
                print y
                res.add(''.join(y))
    return res



# input = ['cat','Bulgaria','nuclear']
input = ['trump']
# read_json_data('50newstune_articles_text_title.json')
parsed_data = read_parsed_data()
res = get_mails(input,parsed_data)

for x in res:
    print x
    print ''


#TODO Take subset of word query results from phrase
#TODO Train on 25000 articles