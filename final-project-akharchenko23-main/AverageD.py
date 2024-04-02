import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
netflix_df = pd.read_csv("netflix_dataset.csv")

# Filter the dataset to include only movies
movies_df = netflix_df[netflix_df['type'] == 'Movie'].copy()  # Make a copy to avoid modifying the original DataFrame

# Convert the duration column to numeric format
movies_df['duration'] = movies_df['duration'].str.replace(' min', '').astype(float)

# Create a bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x=movies_df.index, y='duration', data=movies_df, color='yellow')

# Add a line for the median duration
median_duration = movies_df['duration'].median()
plt.axhline(y=median_duration, color='red', linestyle='--', label=f'Median Duration: {median_duration:.2f} min')

# Customize the plot
plt.title('Duration of Movies')
#plt.xlabel('Movie Index')
plt.ylabel('Duration (minutes)')
plt.legend()

# Rotate x-axis labels for better readability
#plt.xticks(rotation=90)

plt.show()
