import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.corpus import stopwords
from collections import Counter
import pandas as pd
import numpy as np

df = pd.read_csv("pew.csv")
q20 = [x for x in list(df['q20vb']) if type(x) == str]
all_words = ' '.join(q20).split()
all_words = [i.lower() for i in all_words if i.isalpha()]
stop_words = stopwords.words('english') + ['u', 'todo', 'as', 'got', 'didnt', 'thing', 'way', 'get', 'thats', 'would', 'dont',
                                          'thought', 'was\'t', 'wasnt', 'think', 'reason', 'day', 'like', 'por', 'better',
                                          'people', 'marry', 'wanted', 'important', 'wife', 'reason', 'married', 'never',
                                          'one', 'brought', 'cause', 'rest', 'person', 'right', 'la', 'religous', 'marriage', 
                                          'ago', 'knew', 'e', 'day', 'without', 'cuz', 'man', 'que', 'religion', 'make', 'u',
                                          'husband', 'know', 'well', 'loved']
BagOfWords = [lemmatizer.lemmatize(i) for i in all_words if i not in stop_words] 
BagOfWords = [i for i in BagOfWords if i not in stop_words]
#freq = Counter(BagOfWords)
#freq.most_common()[:30]
txt = ' '.join(BagOfWords)

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
wc = WordCloud(background_color="white", width=1000, height=500, max_words=30)
wc.generate(txt)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.axis("off")
plt.show()

wc.to_file("wordcloud.jpg")
