# -*- coding: iso-8859-1 -*-
import nltk

texto = "O NLTK é uma plataforma líder para criar programas em Python para trabalhar com dados em linguagem humana"

frases = nltk.tokenize.sent_tokenize(texto)
print(frases)

tokens = nltk.word_tokenize(texto)
print(tokens)

classes = nltk.pos_tag(tokens)
print(classes)

#entidades
entidades = nltk.chunk.ne_chunk(classes)
print(entidades)