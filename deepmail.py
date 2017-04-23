import os
import pandas as pd
import nltk
import gensim
from gensim import corpora, models, similarities
import json

sentences = []
with open('50newstune_articles_text_title.json') as json_data:
    for line in json_data:
        article = {}
        article = json.loads(line)
        title = nltk.word_tokenize(article['title'].lower())
        text = nltk.word_tokenize(article['text'].lower())
        sentences.append(title)
        sentences.append(text)

        # unicodedata.normalize('NFKD',article['title'].decode('utf-8')).encode('ascii','ignore')

# model = gensim.models.Word2Vec(sentences, size = 200, workers=4)

# model.save('testmodel')
# model = gensim.models.Word2Vec.load('testmodel')
# print 'here'
# for x in model.wv.most_similar(['cat']):
#     print x

# print model.doesnt_match("Trump Obama Putin tennis".split())
#model.most_similar([vector])

for x in sentences:
    if 'cat' in x and 't-shirt' in x:
        print x

# for x in sentences:
#     if 'cat' in x:
#         if('t-shirt' in x):
#             print ' '.join(x)
#             print ''
#         if('ankle' in x):
#             print ' '.join(x)
#             print ''
#         if('spectator' in x):
#             print ' '.join(x)
#             print ''
#     if 'ankle' in x:
#         if('t-shirt' in x):
#             print ' '.join(x)
#             print ''
#         if('spectator' in x):
#             print ' '.join(x)
#             print ''
#     if 't-shirt' in x:
#         if('spectator' in x):
#             print ' '.join(x)
#             print ''