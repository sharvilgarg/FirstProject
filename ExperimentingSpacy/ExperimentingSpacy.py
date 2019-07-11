import spacy
import en_core_web_sm
from spacy import displacy

nlp = en_core_web_sm.load()

ex = input("Enter the sentence")
doc = nlp(ex)
for x in doc:
    print([x, x.lemma_])
print("These are the entities!")
for y in doc.ents:
    print([y, y.label_])
for z in doc:
    print([z,z.has_vector,z.vector_norm])

displacy.serve(doc,style="dep")
