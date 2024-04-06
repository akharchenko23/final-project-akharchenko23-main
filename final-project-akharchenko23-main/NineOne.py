import pandas as pd
import matplotlib.pyplot as plt

# Load the Netflix dataset into a Pandas DataFrame
netflix_data = pd.read_csv("netflix_dataset.csv")

# Cleaning the 'date_added' column
netflix_data['date_added'] = netflix_data['date_added'].str.strip()

# Extracting month information from the 'date_added' column
netflix_data['month_added'] = pd.to_datetime(netflix_data['date_added']).dt.month

# Define seasons
seasons = {
    'Spring': [3, 4, 5],
    'Summer': [6, 7, 8],
    'Autumn/Fall': [9, 10, 11],
    'Winter': [12, 1, 2]
}

# Function to categorize each entry into a season
def get_season(month):
    for season, months in seasons.items():
        if month in months:
            return season

# Apply the function to create a new column for the season
netflix_data['season'] = netflix_data['month_added'].apply(get_season)

# Count the number of entries produced in each season
season_counts = netflix_data['season'].value_counts()

# Plotting the bar chart
plt.figure(figsize=(10, 6))
season_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Titles Added to Netflix by Season')
plt.xlabel('Season')
plt.ylabel('Number of Titles Added')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


