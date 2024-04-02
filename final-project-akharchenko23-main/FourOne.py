import pandas as pd

# Load the dataset
netflix_df = pd.read_csv("netflix_dataset.csv")

# Filter the dataset to include only movies
movies_df = netflix_df[netflix_df['type'] == 'Movie'].copy()  # Make a copy to avoid modifying the original DataFrame

# Convert the duration column to numeric format
movies_df['duration'] = movies_df['duration'].str.replace(' min', '').astype(float)

# Calculate the average duration of movies
average_duration = movies_df['duration'].mean()

print(f"Average duration of movies: {average_duration:.2f} minutes")
