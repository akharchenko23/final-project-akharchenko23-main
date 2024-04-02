import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Завантаження даних Netflix
netflix_data = pd.read_csv('netflix_dataset.csv')

# Фільтрація фільмів та телесеріалів
movies = netflix_data[netflix_data['type'] == 'Movie']
tv_shows = netflix_data[netflix_data['type'] == 'TV Show']

# Групування за рік випуску для фільмів і телесеріалів
movies_by_year = movies['release_year'].value_counts().sort_index()
tv_shows_by_year = tv_shows['release_year'].value_counts().sort_index()

# Вирівнювання років для телесеріалів
merged_index = movies_by_year.index.union(tv_shows_by_year.index)
movies_by_year = movies_by_year.reindex(merged_index, fill_value=0)
tv_shows_by_year = tv_shows_by_year.reindex(merged_index, fill_value=0)

# Визначення ширини стовпців
bar_width = 0.35

# Створення числових індексів для років
years = np.arange(len(merged_index))

# Створення графіку
plt.figure(figsize=(35, 6))

# Додавання стовпців для фільмів
plt.bar(years - bar_width/2, movies_by_year, bar_width, color='b', label='Movies')

# Додавання стовпців для телесеріалів
plt.bar(years + bar_width/2, tv_shows_by_year, bar_width, color='r', label='TV Shows', alpha=0.7)  # alpha - прозорість

plt.title('Amount of Netflix Content by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.xticks(years, merged_index)  # Встановлення позначок на осі x для років
plt.legend()  # Додавання легенди
plt.tight_layout()
plt.show()
