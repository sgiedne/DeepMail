import os
import pandas as pd
import nltk
import gensim
from gensim import corpora, models, similarities
import json

# sentences = []


def read_json_corpus(fname):
	with open(fname) as json_data:
	    for line in json_data:
	        article = {}
	        article = json.loads(line)
	        yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(article['text']), nltk.word_tokenize(article['title'].lower()))
	        # label = nltk.word_tokenize(article['title'].lower())
	        # text = nltk.word_tokenize(article['text'].lower())
	        # docLabels.append(label)
	        # data.append(text)

	        # unicodedata.normalize('NFKD',article['title'].decode('utf-8')).encode('ascii','ignore')

def read_corpus(fname, tokens_only=False):
    with smart_open.smart_open(fname, encoding="iso-8859-1") as f:
        for i, line in enumerate(f):
            if tokens_only:
                yield gensim.utils.simple_preprocess(line)
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])


def read_json_corpus_titles(fname):
	with open(fname) as json_data:
	    for i,line in enumerate(json_data):
	        article = {}
	        article = json.loads(line)
	        yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(article['text']), [i])



train_corpus = list(read_json_corpus_titles('50newstune_articles_text_title.json'))
# print train_corpus[:2]


model = gensim.models.doc2vec.Doc2Vec(size=200, min_count=2, iter=55, workers = 4)

model.build_vocab(train_corpus)

model.train(train_corpus, total_examples=model.corpus_count)


inferred_vector = model.infer_vector(nltk.word_tokenize("A picture shows Pooh the cat using his two bionic legs in Sofia's Central Vet Clinic".lower()))
sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))


print('Test Document ({}): <<{}>>\n'.format('Test', ' '.join(['bulgaria','stray','cat','pooh'])))
print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % model)
for label, index in [('MOST', 0), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
    print(u'%s %s: <<%s>>\n' % (label, sims[index], ' '.join(train_corpus[sims[index][0]].words)))