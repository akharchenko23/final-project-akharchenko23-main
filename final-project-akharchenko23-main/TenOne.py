import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Netflix dataset
netflix_data = pd.read_csv('netflix_dataset.csv')

tv_shows_data = netflix_data[netflix_data['type'] == 'TV Show']


# Correlation analysis for TV shows
tv_shows_correlation = tv_shows_data.groupby('duration')['rating'].value_counts(normalize=True).unstack()

# Print correlation analysis results for TV shows
print("\nCorrelation between TV Show Duration and Ratings:")
print(tv_shows_correlation)

# Create heatmap for TV shows correlation
plt.figure(figsize=(12, 8))
sns.heatmap(tv_shows_correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation between TV Show Duration and Ratings')
plt.xlabel('Rating')
plt.ylabel('Duration')
plt.show()


