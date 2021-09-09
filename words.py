import random
def load_words():
    f=open('words.txt','r') 
    data=f.read().split()
    empty=[]
    for word_list in data:
        empty.append(word_list)
    return empty
def choose_word():
    empty=load_words()
    secrete_word=random.choice(empty)
    secrete_word=secrete_word.lower()
    return secrete_word
choose_word()
