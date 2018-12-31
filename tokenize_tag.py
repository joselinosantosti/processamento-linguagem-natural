import nltk
frase = "Oi eu sou o NLTK, programador"

#separa a frase em palavras
tokens = nltk.word_tokenize(frase)

#mostra as palavras separadas por aspas simples e virgula
print(tokens)

#classifica cada palavra
tagged = nltk.pos_tag(tokens)
print(tagged[0:6])
