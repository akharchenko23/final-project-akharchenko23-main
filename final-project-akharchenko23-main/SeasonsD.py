import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
netflix_df = pd.read_csv("netflix_dataset.csv")

# Filter the dataset to include only TV shows
tv_shows_df = netflix_df[netflix_df['type'] == 'TV Show'].copy()  # Make a copy to avoid modifying the original DataFrame

# Extract the number of seasons from the 'duration' column
tv_shows_df.loc[:, 'num_seasons'] = tv_shows_df['duration'].str.split().str[0].astype(float)

# Calculate the frequency of TV shows for each number of seasons
seasons_distribution = tv_shows_df['num_seasons'].value_counts().sort_index()

# Visualize the distribution
plt.figure(figsize=(10, 6))
seasons_distribution.plot(kind='bar', color='skyblue')
plt.title('Distribution of TV Shows by Number of Seasons')
plt.xlabel('Number of Seasons')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Print the frequency of TV shows for each number of seasons
print("Frequency of TV Shows by Number of Seasons:")
print(seasons_distribution)

