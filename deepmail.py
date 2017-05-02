import os
import pandas as pd
import nltk
import gensim
from gensim import corpora, models, similarities
import json
import unicodedata

sentences = []
with open('50newstune_articles_text_title.json') as json_data:
    for line in json_data:
        article = {}
        article = json.loads(line)
        title = nltk.word_tokenize(unicodedata.normalize('NFKD', article['title']).encode('ascii','ignore'))
        text = nltk.word_tokenize(unicodedata.normalize('NFKD', article['text']).encode('ascii','ignore'))
        sentences.append(title)
        sentences.append(text)

        # unicodedata.normalize('NFKD',article['title'].decode('utf-8')).encode('ascii','ignore')

# model = gensim.models.Word2Vec(sentences, size = 200, workers=4)

# model.save('testmodel')

input = ['cat','Pooh','bionic']

def get_similar(bow):
    model = gensim.models.Word2Vec.load('testmodel')
    return model.wv.most_similar(bow, topn=30)

list_depth0 = get_similar(input)

search_result = []

for x in range(0,3):
    search_result.append([input,list_depth0[x][0]])
    list_depth1 = get_similar([input,list_depth0[x][0]])
    search_result.append([list_depth0[x][0], list_depth1[x][0]])
    search_result.append([input, list_depth1[x][0]])
    search_result.append([input, list_depth0[x][0], list_depth1[x][0]])


res = set()
for x in search_result:
    for y in sentences:
        if len(x) == 3:
            if x[0] in y and x[1] in y and x[2] in y:
                res.add(' '.join(y))
                # print ''
        else:
            if x[0] in y and x[1] in y:
                res.add(' '.join(y))
                # print ''

for x in res:
    print x
    print ''