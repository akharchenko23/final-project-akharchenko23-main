import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the Netflix dataset
netflix_data = pd.read_csv('netflix_dataset.csv')

# Filter movies and TV shows
movies = netflix_data[netflix_data['type'] == 'Movie']
tv_shows = netflix_data[netflix_data['type'] == 'TV Show']

# Get unique rating categories
rating_categories = netflix_data['rating'].unique()

# Initialize lists to store counts for movies and TV shows by rating category
movies_counts = []
tv_shows_counts = []

# Iterate over each rating category
for rating in rating_categories:
    # Count movies and TV shows for each rating category
    movies_counts.append(movies[movies['rating'] == rating].shape[0])
    tv_shows_counts.append(tv_shows[tv_shows['rating'] == rating].shape[0])

# Set the width of the bars
bar_width = 0.35

# Set the positions of the bars on the x-axis
r1 = np.arange(len(rating_categories))
r2 = [x + bar_width for x in r1]

# Create the grouped bar plot
plt.figure(figsize=(10, 6))
plt.bar(r1, movies_counts, color='b', width=bar_width, edgecolor='grey', label='Movies')
plt.bar(r2, tv_shows_counts, color='y', width=bar_width, edgecolor='grey', label='TV Shows')

# Add labels and title
plt.xlabel('Rating', fontweight='bold')
plt.ylabel('Number of Titles', fontweight='bold')
plt.xticks([r + bar_width / 2 for r in range(len(rating_categories))], rating_categories)
plt.title('Distribution of Content by Ratings and Type')

# Add legend
plt.legend()

# Show plot
plt.tight_layout()
plt.show()

# Print distribution of movies and TV shows by ratings
print("Distribution of movies by ratings:")
for rating, count in zip(rating_categories, movies_counts):
    print(f"{rating}: {count}")

print("\nDistribution of TV shows by ratings:")
for rating, count in zip(rating_categories, tv_shows_counts):
    print(f"{rating}: {count}")