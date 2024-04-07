# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # Load the dataset
# netflix_data = pd.read_csv('netflix_dataset.csv')
#
# # Filter for movies only
# movies_data = netflix_data[netflix_data['type'] == 'Movie']
#
# # Extract relevant columns
# duration_rating_data = movies_data[['duration', 'rating']]
#
# # Clean the data
# # Replace non-numeric characters and convert to numeric
# duration_rating_data['duration'] = duration_rating_data['duration'].str.extract('(\d+)').astype(float)
#
# # Impute missing values with median duration
# median_duration = duration_rating_data['duration'].median()
# duration_rating_data['duration'].fillna(median_duration, inplace=True)
#
# # Convert duration to integer
# duration_rating_data['duration'] = duration_rating_data['duration'].astype(int)
#
# # Create a heatmap
# plt.figure(figsize=(10, 6))
# heatmap_data = duration_rating_data.groupby(['duration', 'rating']).size().unstack()
# sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt='.0f', linewidths=.5)
# plt.title('Correlation Between Movie Duration and Ratings')
# plt.xlabel('Rating')
# plt.ylabel('Duration (minutes)')
# plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
netflix_data = pd.read_csv('netflix_dataset.csv')

# Filter for movies only
movies_data = netflix_data[netflix_data['type'] == 'Movie']

# Extract relevant columns
duration_rating_data = movies_data[['duration', 'rating']]

# Clean the data
# Replace non-numeric characters and convert to numeric
duration_rating_data['duration'] = duration_rating_data['duration'].str.extract('(\d+)').astype(float)

# Impute missing values with median duration
median_duration = duration_rating_data['duration'].median()
duration_rating_data['duration'].fillna(median_duration, inplace=True)

# Create bins for durations
bins = [0, 50, 100, 150, 200, 250, 300]
labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300']
duration_rating_data['duration_bins'] = pd.cut(duration_rating_data['duration'], bins=bins, labels=labels)

# Create a heatmap
plt.figure(figsize=(10, 6))
heatmap_data = duration_rating_data.groupby(['duration_bins', 'rating']).size().unstack()
sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt='.0f', linewidths=.5)
plt.title('Correlation Between Movie Duration and Ratings')
plt.xlabel('Rating')
plt.ylabel('Duration (minutes)')
plt.show()
