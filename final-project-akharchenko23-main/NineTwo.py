import pandas as pd
import matplotlib.pyplot as plt
import re

# Load the Netflix dataset into a Pandas DataFrame
netflix_df = pd.read_csv("netflix_dataset.csv")

# Fill NaN values in the 'date_added' column with empty strings
netflix_df['date_added'] = netflix_df['date_added'].fillna('')

# Clean up date_added column using regex to remove leading/trailing spaces
netflix_df['date_added'] = netflix_df['date_added'].apply(lambda x: re.sub(r"^\s+|\s+$", "", str(x)))

# Convert date_added column to datetime with specified format
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'], format='%B %d, %Y', errors='coerce')

# Drop rows with missing dates (if any)
netflix_df.dropna(subset=['date_added'], inplace=True)

# Extract release year and genre information
netflix_df['release_year'] = netflix_df['date_added'].dt.year
netflix_df['genre_list'] = netflix_df['listed_in'].str.split(', ')

# Explode the DataFrame to have one row for each genre
netflix_df_exploded = netflix_df.explode('genre_list')

# Group by release year and genre, then count the number of files in each category
genre_counts_by_year = netflix_df_exploded.groupby(['release_year', 'genre_list']).size().unstack(fill_value=0)

# Plotting
plt.figure(figsize=(16, 10))  # Increased figure size
genre_counts_by_year.plot(kind='bar', stacked=True, colormap='tab20')
plt.title('Netflix Library Growth by Genre Over Time')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')  # Reduced legend font size
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust margins manually to accommodate all decorations
plt.margins(0.05, 0.1)

plt.tight_layout()
plt.show()






