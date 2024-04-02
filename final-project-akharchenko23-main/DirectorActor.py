import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Load the dataset
netflix_df = pd.read_csv("netflix_dataset.csv")

# Specify the format string to handle the date format inconsistency
netflix_df['release_year'] = pd.to_datetime(netflix_df['date_added'], format='%B %d, %Y', errors='coerce').dt.year

# Split the 'listed_in' column by ',' and create a list of genres for each row
netflix_df['genre_list'] = netflix_df['listed_in'].str.split(', ')

# Create a list of all genres
all_genres = [genre for sublist in netflix_df['genre_list'].dropna() for genre in sublist]

# Get unique genres
unique_genres = list(set(all_genres))

# Create a DataFrame to store genre counts for each release year
genre_counts_by_year = pd.DataFrame(index=unique_genres, columns=range(2008, 2023)).fillna(0)

# Count the occurrences of each genre for each release year
for index, row in netflix_df.iterrows():
    if not pd.isna(row['release_year']):  # Check for NaN values in 'release_year'
        for genre in row['genre_list']:
            genre_counts_by_year.loc[genre, row['release_year']] += 1

# Plot the trends in genre popularity over time
plt.figure(figsize=(12, 8))
for genre in genre_counts_by_year.index:
    plt.plot(genre_counts_by_year.loc[genre], label=genre)
plt.title('Trends in Genre Popularity Over Time')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.xticks(range(2008, 2023), rotation=45)
plt.show()


