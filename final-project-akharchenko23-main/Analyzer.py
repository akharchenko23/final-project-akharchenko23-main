import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the Netflix dataset
netflix_data = pd.read_csv('netflix_dataset.csv')

# Filtering movies and TV shows
movies = netflix_data[netflix_data['type'] == 'Movie']
tv_shows = netflix_data[netflix_data['type'] == 'TV Show']

# Grouping by release year for movies and TV shows
movies_by_year = movies['release_year'].value_counts().sort_index()
tv_shows_by_year = tv_shows['release_year'].value_counts().sort_index()

# Aligning years for TV shows
merged_index = movies_by_year.index.union(tv_shows_by_year.index)
movies_by_year = movies_by_year.reindex(merged_index, fill_value=0)
tv_shows_by_year = tv_shows_by_year.reindex(merged_index, fill_value=0)

# Determining the width of the bars
bar_width = 0.35

# Creating numerical indices for years
years = np.arange(len(merged_index))

# Print key details
print("Total number of movies:", movies.shape[0])
print("Total number of TV shows:", tv_shows.shape[0])
print()

# Print distribution of movies and TV shows among years
print("Distribution of movies among years:")
print(movies_by_year)
print()

print("Distribution of TV shows among years:")
print(tv_shows_by_year)
print()

# Creating the plot
plt.figure(figsize=(25, 6))

# Adding bars for movies
plt.bar(years - bar_width/2, movies_by_year, bar_width, color='b', label='Movies')

# Adding bars for TV shows
plt.bar(years + bar_width/2, tv_shows_by_year, bar_width, color='r', label='TV Shows', alpha=0.7)

plt.title('Amount of Netflix Content by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.xticks(years, merged_index)  # Setting x-axis labels for years
plt.xticks(rotation=45)
plt.legend()  # Adding legend
plt.tight_layout()
plt.show()
