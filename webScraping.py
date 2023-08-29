import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the URL
url = 'http://codewithharry.com'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find specific elements on the page using CSS selectors
titles = soup.select('h2.title')

# Extract and print the text from the selected elements
for title in titles:
    print(title.text)
