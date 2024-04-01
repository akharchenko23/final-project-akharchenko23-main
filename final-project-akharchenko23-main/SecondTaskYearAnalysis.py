import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# The histogram shows the distribution of content (movies or TV shows)
# based on their release year. Each bar on the histogram represents a range of years, and the
# height of the bar indicates the count of content released within that range.

# Load the dataset
netflix_df = pd.read_csv("netflix_dataset.csv")

# Plot the distribution of content by release year
plt.figure(figsize=(12, 6))
sns.histplot(netflix_df['release_year'],
             bins=range(int(netflix_df['release_year'].min()), int(netflix_df['release_year'].max()) + 1, 1), kde=False,
             color='skyblue')
plt.title('Distribution of Content by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()
