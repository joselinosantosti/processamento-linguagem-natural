from nltk.book import *

#procurando a palavra Adam
text3.concordance("Adam")

#procurando palavras similares a earth
print('SIMILARES')
text3.similar("earth")

#contextos comuns
print('CONTEXTOS COMUNS')
text3.common_contexts(["God", "Adam"])
