import requests
from bs4 import BeautifulSoup as bs
import json
import re
import pymongo
from pymongo import MongoClient
import sys

# Website url to parse data from
# website_url = 'https://en.wikipedia.org/wiki/Category:The_Lord_of_the_Rings'
website_url = str(sys.argv[1])
# Json Data template as python dictionary
json_data = {
    'name': "",
    'subCategories': [],
    'pages': [],
    'files': []
}
# CSS Selector queries for beautifulsoup
queries = {"subCategories": "div.CategoryTreeItem a", "pages": "div#mw-pages ul a", "files": "div#mw-category-media ul a"}
port = 27017

# Get the html from the url and return the beautifulsoup object to use in parsing
def setupSoup(website_url):
    try:
        html_doc = requests.get(website_url).text
        soup = bs(html_doc, 'html.parser')
        return soup
    # A very generic exception handling, something more sophisticated could be written to better guide the user.
    except requests.exceptions.RequestException as e:
        print(e)

# Build and return the parsed JSON data
def buildJson(queries,soup,json_data,website_url):
    # Set the category name if the URL is a valid wikipedia category URL
    if(re.search("https://en.wikipedia.org/wiki/Category:", website_url)):
        json_data["name"] = website_url.split("Category:")[1]
    # Parse the data for each query
    for query in queries:
        for item in soup.select(queries[query]):
            url = "https://en.wikipedia.org" + item.get("href")
            content = item.text
            data = {'name': content, 'url': url}
            json_data[query].append(data)
    return json_data

# Setup the mongo database and insert the jsondata into a collection
def setupDB(port,json_data):
    client = MongoClient('localhost', port)
    db = client.categories_db
    collection = db.parsed_categories
    # Empty the collection before inserting data. This is for testing purposes
    #collection.delete_many({})
    collection.insert_one(json_data)
    return client

soup = setupSoup(website_url)
json_data = buildJson(queries,soup,json_data,website_url)
client = setupDB(port,json_data)