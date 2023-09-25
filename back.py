import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import PorterStemmer
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

word_data = "Wow, NLTK is really powerful!"
nltk_tokens = nltk.word_tokenize(word_data)
print (nltk_tokens)

#Here we tokenized the text to seperate the sentence into different parts

tokens_without_sw = [word for word in nltk_tokens if not word in stopwords.words()]

print(tokens_without_sw)

ps = PorterStemmer()
for w in nltk_tokens:
	rootWord=ps.stem(w)
	print(rootWord)
	
polar= SentimentIntensityAnalyzer()
filter=(' '.join(nltk_tokens))
print(filter)
print(polar.polarity_scores(filter))