import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
netflix_df = pd.read_csv("netflix_dataset.csv")

# Split the 'country' column by ',' and create a list of countries for each row
netflix_df['country_list'] = netflix_df['country'].str.split(', ')

# Create a list of all countries
all_countries = [country for sublist in netflix_df['country_list'].dropna() for country in sublist]

# Count the occurrences of each country
country_counts = pd.Series(all_countries).value_counts()

# Visualize the distribution of content by country
plt.figure(figsize=(30, 6))
country_counts[:25].plot(kind='bar', color='yellow')
plt.title('Top 20 Countries by Content Volume')
plt.xlabel('Country')
plt.ylabel('Number of Titles')
plt.xticks(rotation=25)
plt.grid(axis='y')
plt.show()
