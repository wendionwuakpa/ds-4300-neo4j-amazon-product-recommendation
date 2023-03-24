from neo4j import GraphDatabase
import pandas as pd
import numpy as np

uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"
driver = GraphDatabase.driver(uri, auth=(username, password))

spotify_data = pd.read_csv("spotify.csv")

# Filter the data set to only include the three Regina Spektor songs 
regina_songs = ['The Call', 'Two Birds', 'Samson']
regina_data = spotify_data[spotify_data['track_name'].isin(regina_songs)]

sample_size = 1000
remaining_data = spotify_data[spotify_data['track_name'].isin(regina_songs)] # use the negation operator to exclude the Regina Spektor songs
sample_data = remaining_data.sample(n=min(sample_size-len(regina_data), len(remaining_data)), replace=False) 
# Combine the Regina Spektor songs with the sampled data
sample_data = pd.concat([sample_data, regina_data])