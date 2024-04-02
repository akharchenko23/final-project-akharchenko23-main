import pandas as pd
import matplotlib.pyplot as plt

num_of_directors = 20
num_of_actors = 20

# Load the dataset
netflix_df = pd.read_csv("netflix_dataset.csv")

# Split the 'director' column by ',' and create a list of directors for each row
netflix_df['director_list'] = netflix_df['director'].str.split(', ')
# Split the 'cast' column by ',' and create a list of cast members for each row
netflix_df['cast_list'] = netflix_df['cast'].str.split(', ')

# Create a list of all directors and cast members
all_directors = [director for sublist in netflix_df['director_list'].dropna() for director in sublist]
all_cast = [cast for sublist in netflix_df['cast_list'].dropna() for cast in sublist]

# Count the occurrences of each director and cast member
director_counts = pd.Series(all_directors).value_counts()
cast_counts = pd.Series(all_cast).value_counts()

# Visualize the top directors with the most titles
plt.figure(figsize=(12, 6))
director_counts[:num_of_directors].plot(kind='bar', color='skyblue')
plt.title('Directors with the Most Titles on Netflix')
plt.xlabel('Director')
plt.ylabel('Number of Titles')
plt.xticks(rotation=20)
plt.grid(axis='y')
plt.show()

# Visualize the top cast members with the most titles
plt.figure(figsize=(12, 6))
cast_counts[:num_of_actors].plot(kind='bar', color='yellow')
plt.title('Cast Members with the Most Titles on Netflix')
plt.xlabel('Cast Member')
plt.ylabel('Number of Titles')
plt.xticks(rotation=25)
plt.grid(axis='y')
plt.show()
