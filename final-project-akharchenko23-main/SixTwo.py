import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the Netflix dataset
netflix_data = pd.read_csv('netflix_dataset.csv')

netflix_data['actors'] = netflix_data['cast'].str.split(', ')

# Select a specific actor (change actor_name to the desired actor)
actor_name = 'Tom Hanks'

# Filter the dataset to include only rows where the selected actor is present
actor_data = netflix_data[netflix_data['actors'].apply(lambda x: actor_name in x if isinstance(x, list) else False)]

# Create a list of unique directors the actor has collaborated with
directors = actor_data['director'].unique()

# Create a directed graph
G = nx.DiGraph()

# Add nodes (actor and directors)
G.add_node(actor_name)
for director in directors:
    G.add_node(director)

# Add edges (collaborations)
for director in directors:
    G.add_edge(actor_name, director)

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=10, font_weight='bold')
plt.title(f"Collaboration Network: {actor_name} to Directors")
plt.show()

