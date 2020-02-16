import sys
import os
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS

a = os.path.dirname(__file__)

def get_wiki(query):
	title = wikipedia.search(query)[0]
	page = wikipedia.page(title)
	return page.content

def create_wordcloud(text):
	mask = np.array(Image.open(os.path.join(a, "cloud.png")))

	stopwords = set(STOPWORDS)

	wc = WordCloud(background_color="white",
					max_words=100,
					mask=mask,
	               	stopwords=stopwords)

	wc.generate(text)

	wc.to_file(os.path.join(a, "kz.png"))

create_wordcloud(get_wiki("Kazakhstan"))