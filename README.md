# IHRD_PMD_Software_Developer_Backend

# Django Task


## 1.Home Page Accessibility
**Check if email or phone number already exists in registration:**

	if get_user_model().objects.filter(email=email).exists():
	      return Response({'code': 400, 'message': 'Email already exists'})

page accessed successfully

 
## 2.User Registration Functionality:
**User registerd succesfully!!:**	 
      
   
## 3.User Login Functionality:

**Authenticate the user in login function**
        user = get_user_model().objects.filter(email=email).first()
        
**Update last login time**
            user.last_login = timezone.now()
            user.save()
 
**Generate JWT tokens**
  from rest_framework import status
  from rest_framework_jwt.settings import api_settings
            payload = jwt_payload_handler(user)
            access_token = jwt_encode_handler(payload)
            
**login success**

![list](https://github.com/ihsan292292/IHRD_PMD_Software_Developer_Backend/assets/97184876/82b3be48-2cfb-491a-b0ae-f14dccb8a00a)

	
## 4.User Data Retrieval

**Use RetrieveAPIView to retrieve a single model instance (in this case, the authenticated user)**

**Specify the authentication classes that you want to use 				   (SessionAuthentication,TokenAuthentication, etc.) in authentication_classes**

**Use IsAuthenticated permission class to ensure only authenticated users can access this endpoint**
 
**image_name field deleted** in serializer beacause there is no need of an image since image doesnot in APIUser model
 
![Screenshot from 2023-11-23 23-24-45](https://github.com/ihsan292292/IHRD_PMD_Software_Developer_Backend/assets/97184876/ad1b0dff-8fff-4f89-992f-bf5abfe78e23)

 
## 5.Data Import and Visualization:

	**data loaded from json file**
	
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
	    population = entry['pop1980']+entry['pop2000']+entry['pop2010']+entry['pop2022']					+entry['pop2023']+entry['pop2030']+entry['pop2050']
	    cursor.execute("INSERT OR REPLACE INTO CountryPopulation (country, population) VALUES (?, ?)", (country, population))

	# Commit changes and close connection
	conn.commit()
	conn.close()
		
	**viewd in sql table**

	
			  country  population
	0               India  9028361192
	1               China  9174463823
	2       United States  2222562101
	3           Indonesia  1768676464
	4            Pakistan  1547597303
	..                ...         ...
	229        Montserrat       38386
	230  Falkland Islands       23726
	231              Niue       15436
	232           Tokelau       12920
	233      Vatican City        4300
	
	**data visualized in another file**
	
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

 ![Screenshot from 2023-11-24 09-13-06](https://github.com/ihsan292292/IHRD_PMD_Software_Developer_Backend/assets/97184876/e53e2255-2b17-46a7-8b7e-c240daa6c44b)


	def display_population_table(request):
	    queryset = CountryPopulation.objects.all()

	    # Convert queryset to list of dictionaries
	    data = list(queryset.values())  # or values_list() if you need specific fields

	    # Convert data to DataFrame using Pandas
	    df = pd.DataFrame(data)

	    # Convert DataFrame to HTML table representation
	    population_table = df.to_html(classes='table table-striped')

	    return render(request, 'population_table.html', {'population_table': population_table})
	    
	    
## 6.Advanced Search Functionality

	import json
	
	# Load the data from the JSON file
	with open('population_data.json', 'r') as file:
	    data = json.load(file)

	# Define a function for advanced search based on user-defined criteria
	def advanced_search(data, criteria):
	    # Initialize an empty list to store matched results
	    matched_results = []

	    # Iterate through each entry in the dataset
	    for entry in data:
		match = True  # Flag to track if the entry matches all search criteria

		# Check if the entry matches all user-defined criteria
		for key, value in criteria.items():
		    if key in entry:
		        if entry[key] != value:
		            match = False
		            break  # Break out of the loop if any criteria doesn't match

		# If all criteria match, add the entry to matched_results
		if match:
		    matched_results.append(entry)

	    return matched_results

	# Example: Perform an advanced search based on certain criteria
	search_criteria = {
	    "country": "United Kingdom",
	    "pop2023": 67736802,
	    "density": 279.9851
	}

	# Perform the advanced search
	results = advanced_search(data, search_criteria)

	# Display the matched results
	for result in results:
	    print(result)

## 7.Add a Logout button:

	// Logout functionality in JavaScript (example using localStorage)

	// Function to handle logout action
	function logout() {
	  // Remove the token from localStorage or sessionStorage
	  localStorage.removeItem('jwtToken'); // Change 'jwtToken' to your token key

	  // Redirect to the login page or update UI accordingly
	  window.location.href = '/login'; // Redirect to login page
	}
	
	
	
	
# FastAPi Task

**run via :** http://0.0.0.0:5001/

**Setup FastAPI and Pandas:**

**Load Netflix dataset into a Pandas DataFrame**

	netflix_data = pd.read_csv("dataset_netflix.csv")

 **data visualized using pie and bar chart**

 
![Screenshot from 2023-11-24 08-21-28](https://github.com/ihsan292292/IHRD_PMD_Software_Developer_Backend/assets/97184876/8c248364-717f-46c9-932e-1cc751520e14)




![Screenshot from 2023-11-24 08-26-08](https://github.com/ihsan292292/IHRD_PMD_Software_Developer_Backend/assets/97184876/2eb57245-5248-4cc1-8235-20ddcfbebfb5)
