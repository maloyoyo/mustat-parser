import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime



websites = []
with open('websites.txt', 'r') as f:
    for line in f:
        websites.append("https://www.mustat.com/" + line.strip())

# Iterate over the list of websites
for website in websites:
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(website).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")

    # Find all the tables in the page
    tables = soup.find_all('table')

    # Get the table having the traffic data
    traffic_table = tables[1]

    # Get all the rows in the table
    rows = traffic_table.find_all('tr')

    # Get the data from each row
    for row in rows:
        cols = row.find_all('td')
        data = [ele.text.strip() for ele in cols]
        print(data)

# Write the data to the table
# Create a list of lists
data = []
for website in websites:
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(website).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")

    # Find all the tables in the page
    tables = soup.find_all('table')

    # Get the table having the traffic data
    traffic_table = tables[1]

    # Get all the rows in the table
    rows = traffic_table.find_all('tr')

    # Get the data from each row
    for row in rows:
        cols = row.find_all('td')
        data.append([website.replace('https://www.mustat.com/', '')
                    ] + [ele.text.strip() for ele in cols])

# Create a DataFrame from the list of lists
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
now = datetime.datetime.now()
filename = "traffic_data_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
df.to_csv(filename, index=False)
