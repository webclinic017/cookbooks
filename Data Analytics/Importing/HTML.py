# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 20:19:12 2021

@author: LK
"""

from urllib.request import urlopen, Request

"""
- Package and sent a GET request to catch the response afterwards
    > Read the response {hhtp.client.HTTPResponse} using the read() method to extract the html
    > Get a high level interface using the requests module
"""

# Specify the url

url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# This packages the request so that it is available for execution

request = Request(url)

# Send the request and saves the response / catches it. 

response = urlopen(request)

# Print Datatype of response

print(type(response))

# Extract the response with the read() method to get the html

html = response.read()

# Have a look at the html output

print(html)

# Close the response
response.close()

'''
Alternative
'''

import requests

# Specify url

url = 'https://www.python.org/~guido/'

# Package the request, sent it and catch the response using the requests.get method

r = requests.get(url)

# Extract the html of the response

text = r.text

# Print the html

print(text)

from bs4 import BeautifulSoup

# Create a BeautifulSoup object from the html

soup = BeautifulSoup(text)

# Prettify the BeautifulSoup object

pretty_soup = soup.prettify()

# Have a look at this beautiful Soup

print(pretty_soup)

# Get the title of the webpage

title = soup.title
print(title)

# Get the text of the webpage

text = soup.get_text()
print(text)

# Find all the hyperlinks (also knows as 'a'-tags in html)

a_tags = soup.find_all('a')

# Print them to the shell

for link in a_tags:
    print(link.get('href'))








