import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "AI and NLP are essential fields in modern technology."
words = word_tokenize(sentence)
print(pos_tag(words))
