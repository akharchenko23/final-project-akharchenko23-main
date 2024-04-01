import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
netflix_df = pd.read_csv("netflix_dataset.csv")
# Display the first few rows of the dataset
print(netflix_df.head())

# Check the data types of each column
print(netflix_df.dtypes)

# Check for missing values
print(netflix_df.isnull().sum())


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

import seaborn as sns

# Convert date_added column to datetime
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'])

# Extract year from date_added
netflix_df['year_added'] = netflix_df['date_added'].dt.year

# Plot the trend of content added over the years
plt.figure(figsize=(10, 6))
sns.countplot(x='year_added', hue='type', data=netflix_df)
plt.title('Trend of Content Added Over the Years')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Content Type')
plt.show()

