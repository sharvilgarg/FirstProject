"""
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone' \
     ' market and ordered the company to alter its practices'


def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent


sent = preprocess(ex)
print(sent, sep="\n")
"""

from bs4 import BeautifulSoup
import requests
import re
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
# ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone' \
#      ' market and ordered the company to alter its practices'
# doc = nlp(ex)
# print([(X.text, X.label_) for X in doc.ents])
# print("\n")
# print([(X, X.ent_iob_, X.ent_type_) for X in doc])


def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))


ny_bb=input("Enetr a sentence")
article = nlp(ny_bb)

# for x in article:
#     if x.is_stop:
#         print(x)
for x in article:
    print([x,x.text,x.pos_,x.dep_,x.lemma_])
print(len(article.ents))
labels = [x.label_ for x in article.ents]
print(Counter(labels))
items = [x.text for x in article.ents]
print(Counter(items).most_common(3))

sentences = [x for x in article.sents]
print(sentences[20])

print(displacy.render(nlp(str(sentences[19])), style='ent'))

# print([(X.orth_,X.pos_,X.lemma_) for X in [y for y in nlp(str(sentences[20]))
#                                       if not y.is_stop and y.pos_ != 'PUNCT'] ])
# print(dict([(str(x), x.label_) for x in nlp(str(sentences[20])).ents]))
