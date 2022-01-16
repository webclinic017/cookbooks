# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 17:06:29 2021

@author: LK
"""

import requests

# Assign url to variable

url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'

# Package the request, sent it and catch the response

r = requests.get(url)

# Decode the JSON data into a dictionary

json_data = r.json()

# Print out all key-value pairs

for key in json_data:
    print(key + ': ',json_data[key])