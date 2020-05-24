from spacy.lang.en import English
nlp = English()
tokens = nlp("Some\nspaces  and\ttab characters")
tokens_text = [t.text for t in tokens]
assert tokens_text == ["Some", "\n", "spaces", " ", "and", "\t", "tab", "characters"]

import en_core_web_sm
nlp = en_core_web_sm.load()
doc = nlp("This is a sentence.")
print([(w.text, w.pos_) for w in doc])

import spacy
spacy.explain("NORP")
# Nationalities or religious or political groups
doc = nlp("Hello world")
for word in doc:
   print(word.text, word.tag_, spacy.explain(word.tag_))
# Hello UH interjection
# world NN noun, singular or mass
