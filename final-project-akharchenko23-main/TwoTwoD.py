import pandas as pd
import matplotlib.pyplot as plt

# Load the Netflix dataset
netflix_data = pd.read_csv('netflix_dataset.csv')

# Filter movies and TV shows
movies = netflix_data[netflix_data['type'] == 'Movie']
tv_shows = netflix_data[netflix_data['type'] == 'TV Show']

# Calculate number of new movie releases each year
new_movies_by_year = movies.groupby('release_year').size()

# Calculate number of new TV show releases each year
new_tv_shows_by_year = tv_shows.groupby('release_year').size()

# Plot trend of new content releases over time
plt.figure(figsize=(12, 6))

new_movies_by_year.plot(kind='line', marker='o', color='b', label='New Movies')
new_tv_shows_by_year.plot(kind='line', marker='o', color='r', label='New TV Shows')

plt.title('Trend of New Content Releases on Netflix Over Time')
plt.xlabel('Release Year')
plt.ylabel('Number of New Releases')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
