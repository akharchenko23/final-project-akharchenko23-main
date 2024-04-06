import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt
WORDS_NUM = 100
# Load the Netflix dataset into a Pandas DataFrame
netflix_data = pd.read_csv("netflix_dataset.csv")

# Combine titles and descriptions into a single text column
netflix_data['text'] = netflix_data['title'] + ' ' + netflix_data['description']

# Convert text to lowercase
netflix_data['text'] = netflix_data['text'].str.lower()

# Remove special characters and punctuation
netflix_data['text'] = netflix_data['text'].apply(lambda x: re.sub(r'[^\w\s]', '', x))

# Split text into individual words
words = ' '.join(netflix_data['text']).split()

stopwords = set(['the', 'is', 'and', 'a', 'an', 'to', 'of', 'in', 'with', 'his', 'her', 'for', 'on', 'their', 'when', 'this', 'from', 'as', 'by', 'after', 'he', 'that', 'who', 'but', 'at', 'they' ])
words = [word for word in words if word not in stopwords]

# Count the frequency of each word
word_freq = Counter(words)

print("Most common keywords in titles and descriptions:")
print(word_freq.most_common(WORDS_NUM))

common_keywords = [word[0] for word in word_freq.most_common(WORDS_NUM)]
common_keywords_freq = [word[1] for word in word_freq.most_common(WORDS_NUM)]

plt.figure(figsize=(20, 6))
plt.bar(common_keywords, common_keywords_freq, color='yellow')
plt.xlabel('Keywords')
plt.ylabel('Frequency')
plt.title('Most Common Keywords in Netflix Titles and Descriptions')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()

