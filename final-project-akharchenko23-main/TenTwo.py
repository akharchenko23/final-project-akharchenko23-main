import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

netflix_data = pd.read_csv('netflix_dataset.csv')

release_rating_data = netflix_data[['release_year', 'rating']]

release_rating_data.dropna(inplace=True)

# Convert 'release_year' to integer
release_rating_data['release_year'] = release_rating_data['release_year'].astype(int)

plt.figure(figsize=(10, 6))
sns.scatterplot(data=release_rating_data, x='release_year', y='rating')
plt.title('Relationship Between Release Year and Rating')
plt.xlabel('Release Year')
plt.ylabel('Rating')
plt.grid(True)
plt.show()
