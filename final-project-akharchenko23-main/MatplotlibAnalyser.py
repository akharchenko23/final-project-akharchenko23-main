import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
netflix_df = pd.read_csv("netflix_dataset.csv")
# Count the number of movies and TV shows
content_type_counts = netflix_df['type'].value_counts()


# Plot the distribution
plt.figure(figsize=(8, 6))
content_type_counts.plot(kind='bar', color=['skyblue', 'yellow'])
plt.title('Distribution of Movies vs TV Shows')
plt.xlabel('Content Type')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()
