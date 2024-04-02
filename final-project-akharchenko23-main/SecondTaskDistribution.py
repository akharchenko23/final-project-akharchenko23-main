import pandas as pd
import matplotlib.pyplot as plt

# Load the Netflix dataset
netflix_data = pd.read_csv('netflix_dataset.csv')

# Filter movies and TV shows
movies = netflix_data[netflix_data['type'] == 'Movie']
tv_shows = netflix_data[netflix_data['type'] == 'TV Show']

# Group by release year and type
movies_by_year = movies.groupby('release_year').size()
tv_shows_by_year = tv_shows.groupby('release_year').size()

# Plot distribution of movies and TV shows by release year
plt.figure(figsize=(12, 4))

movies_by_year.plot(kind='bar', color='b', label='Movies')
tv_shows_by_year.plot(kind='bar', color='y', label='TV Shows', alpha=0.7)  # Set alpha to adjust transparency

plt.title('Distribution of Netflix Content by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

