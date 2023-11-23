import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from django.shortcuts import render
from users.models import CountryPopulation

# Retrieve data from SQLite database
conn = sqlite3.connect('video_db.db')
df = pd.read_sql_query("SELECT * FROM CountryPopulation", conn)
conn.close()

# Display table of population data
print(df)

# Create a bar graph
plt.figure(figsize=(12, 6))
plt.bar(df['country'], df['population'])
plt.xlabel('Country')
plt.ylabel('Population')
plt.title('Population by Country')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
plt.savefig('population_chart.png')

def display_population_table(request):
    queryset = CountryPopulation.objects.all()

    # Convert queryset to list of dictionaries
    data = list(queryset.values())  # or values_list() if you need specific fields

    # Convert data to DataFrame using Pandas
    df = pd.DataFrame(data)

    # Convert DataFrame to HTML table representation
    population_table = df.to_html(classes='table table-striped')

    return render(request, 'population_table.html', {'population_table': population_table})
