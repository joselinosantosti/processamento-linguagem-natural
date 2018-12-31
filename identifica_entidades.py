import nltk
frase = """Oi eu sou o Watson, programador e gosto da cortana"""
tokens = nltk.word_tokenize(frase)
tagged = nltk.pos_tag(tokens)

entidades = nltk.chunk.ne_chunk(tagged)
print(entidades)