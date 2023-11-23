import sqlite3
import json

# Read JSON file
with open('dataset_world_population_by_country_name.json', 'r') as file:
    data = json.load(file)

# Create a SQLite database connection
conn = sqlite3.connect('video_db.db')
cursor = conn.cursor()

# Create a table to store population data
cursor.execute('''CREATE TABLE IF NOT EXISTS CountryPopulation (
                    country TEXT PRIMARY KEY,
                    population INTEGER
                )''')

# Insert data into the SQLite database
for entry in data:
    country = entry['country']
    population = entry['pop1980']+entry['pop2000']+entry['pop2010']+entry['pop2022']+entry['pop2023']+entry['pop2030']+entry['pop2050']
    cursor.execute("INSERT OR REPLACE INTO CountryPopulation (country, population) VALUES (?, ?)", (country, population))

# Commit changes and close connection
conn.commit()
conn.close()