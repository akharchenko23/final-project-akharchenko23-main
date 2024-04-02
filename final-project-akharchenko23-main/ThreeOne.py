import pandas as pd
import matplotlib.pyplot as plt

# Load the Netflix dataset
netflix_data = pd.read_csv('netflix_dataset.csv')

# 1. Explore the distribution of content by ratings
ratings_distribution = netflix_data['rating'].value_counts()

# Plotting the distribution of content by ratings
plt.figure(figsize=(10, 6))
ratings_distribution.plot(kind='bar')
plt.title('Distribution of Content by Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Displaying the ratings distribution
print("Distribution of content by ratings:")
print(ratings_distribution)
