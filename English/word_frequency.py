# no case of specifial characters is resolved in this code 
#  i will resolve it in latter
from collections import Counter
from tabulate import tabulate

text="I myself is a pure disappointment. It was me who tied the strings of my heart with my own hands, and whenever i open my arms to fly it pulled my heart ,always left me bleeding inside out "
word=""
words=list()
sentence=""
sentences=list()


for char in text:
    if char=='.' or char=='?':
        if sentence:
            sentences.append(sentence)
            sentence=""
    else:
            sentence+=char

if sentence:
    sentences.append(sentence)
    
# print(sentences)


for char in text :
    if char.isspace():
        if word:  # Avoid appending empty words
            words.append(word.lower())
            word = ""
    else:
        word += char 
if word:
    words.append(word.lower())  


print(words)


#  frequency 
word_freq = Counter(words)
# print(word_freq)

table_data = [(key, value) for key, value in word_freq.items()]

print(tabulate(table_data, headers=["Word", "Frequency"], tablefmt="grid"))

