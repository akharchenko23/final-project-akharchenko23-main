
import pandas as pd
import matplotlib.pyplot as plt

# Load the Netflix dataset
netflix_data = pd.read_csv('netflix_dataset.csv')
new_content_by_year = netflix_data.groupby('release_year').size()

# Plot trend of new content releases over time
plt.figure(figsize=(12, 6))
new_content_by_year.plot(kind='line', marker='o', color='b')
plt.title('Trend of New Content Releases on Netflix Over Time')
plt.xlabel('Release Year')
plt.ylabel('Number of New Releases')
plt.grid(True)
plt.tight_layout()
plt.show()
