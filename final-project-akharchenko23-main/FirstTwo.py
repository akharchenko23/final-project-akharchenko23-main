import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
netflix_df = pd.read_csv("netflix_dataset.csv")

# Drop rows with missing date_added values
netflix_df = netflix_df.dropna(subset=['date_added'])

# Convert date_added column to datetime with custom format
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'], format='%B %d, %Y', errors='coerce')

# Drop rows where conversion fails
netflix_df = netflix_df.dropna(subset=['date_added'])

# Extract year from date_added
netflix_df['year_added'] = netflix_df['date_added'].dt.year

# Plot the trend of content added over the years
plt.figure(figsize=(10, 5))
sns.countplot(x='year_added', hue='type', data=netflix_df)
plt.title('Trend of Content Added Over the Years')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Content Type')
plt.show()

# Check for duplicates
duplicate_rows = netflix_df[netflix_df.duplicated()]
#print("Duplicate Rows:")
#print(duplicate_rows)

movie_counts = netflix_df[netflix_df['type'] == 'Movie'].groupby('year_added').size()
tv_show_counts = netflix_df[netflix_df['type'] == 'TV Show'].groupby('year_added').size()

print("Movie Counts by Year:")
print(movie_counts)

print("TV Shows Counts by Year:")
print(tv_show_counts)

total_actual_movies = netflix_df['type'].value_counts()['Movie']
total_actual_tvshows = netflix_df['type'].value_counts()['TV Show']
print("Total Movies:", total_actual_movies)
print("Total TV Shows:", total_actual_tvshows)

