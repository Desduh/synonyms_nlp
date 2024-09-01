import spacy

import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')

nlp = spacy.load('en_core_web_sm')

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    if word in synonyms:
        synonyms.remove(word)
    return list(synonyms)

def replace_synonyms(sentence):
    doc = nlp(sentence)
    new_sentence = []
    
    for token in doc:
        if token.pos_ in ["NOUN", "VERB", "ADJ", "ADV"]: 
            synonyms = get_synonyms(token.text.lower())
            if synonyms:
                synonym = synonyms[0].replace('_', ' ')
                new_sentence.append(synonym)
            else:
                new_sentence.append(token.text)
        else:
            new_sentence.append(token.text)
    
    return " ".join(new_sentence)


key = True
while key: 

    sentence = input(str("Sentence: "))
    rewritten_sentence = replace_synonyms(sentence)
    print("Replaced by synonyms:", rewritten_sentence)
    print("")
    
    if ("s" == input(str("Exit s/n: "))):
        key = False
