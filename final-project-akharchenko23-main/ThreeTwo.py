import pandas as pd
import matplotlib.pyplot as plt

NUM_OF_COUNTRIES = 30

# Load the Netflix dataset into a DataFrame and drop rows with missing values in the 'rating' and 'country' columns
netflix_data = pd.read_csv('netflix_dataset.csv')
netflix_data.dropna(subset=['rating', 'country'], inplace=True)

# Extract regions from countries (assuming regions are separated by ',')
netflix_data['region'] = netflix_data['country'].apply(lambda x: x.split(',')[0].strip())

# Get the top 10 countries with the most titles
top_countries = netflix_data['region'].value_counts().nlargest(NUM_OF_COUNTRIES).index

# Filter the data to include only the top 10 countries
netflix_data = netflix_data[netflix_data['region'].isin(top_countries)]

# Get all unique ratings present in the filtered dataset
unique_ratings = sorted(netflix_data['rating'].unique())

# Group the filtered data by 'region' and 'rating', and count the number of entries
grouped_data = netflix_data.groupby(['region', 'rating']).size().unstack(fill_value=0)

# Create a colormap with enough distinct colors to cover all unique ratings
num_ratings = len(unique_ratings)
cmap = plt.get_cmap('tab20', num_ratings)

# Plot the bar chart
plt.figure(figsize=(15, 8))

# Iterate over each rating and plot a bar for each country using the corresponding color
for i, rating in enumerate(unique_ratings):
    color = cmap(i)
    bars = plt.bar(grouped_data.index, grouped_data[rating], color=color, label=rating)

for region in grouped_data.index:
        ratings_counts = "; ".join([f"{rating}: {count}" for rating, count in grouped_data.loc[region].items() if count >= 1])
        print(f'{region}: {ratings_counts}')


plt.title('Number of Titles by Rating and Region')
plt.xlabel('Region')
plt.ylabel('Number of Titles')
plt.xticks(rotation=90)  # Rotate country labels for better readability
plt.legend(title='Rating', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()




