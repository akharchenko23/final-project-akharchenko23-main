import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("netflix_dataset.csv")
# Group the dataset by release year and count the number of content releases for each year
content_by_year = netflix_df.groupby('release_year').size().reset_index(name='count')

# Plot the trend of content production over the years
plt.figure(figsize=(12, 6))
sns.lineplot(x='release_year', y='count', data=content_by_year, marker='o', color='red')
plt.title('Trend of Content Production Over the Years')
plt.xlabel('Release Year')
plt.ylabel('Count of New Content')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()