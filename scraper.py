import requests
import bs4
import json
import time
import random

jobs = []

# Headers to fake the request as a browser to avoid blocking
headers = open("headers.json")
headers = dict(json.load(headers))

def scrape_data(search_query="mern stack developer"):
    time.sleep(random.randint(1, 5))
    search_query = search_query.replace(" ", "%20")
    # Sends a request
    url = requests.get(f"https://www.upwork.com/nx/search/jobs/?q={search_query}&sort=recency", headers=headers)

    # Parses the HTML output
    parser = bs4.BeautifulSoup(url.content, 'lxml')

    # Extract titles using a loop for better readability
    titles = []
    for title_elem in parser.find_all('h2', class_="h5 mb-0 mr-2 job-tile-title"):
        titles.append(title_elem.text.replace("\n", ""))

    # Extract URLs using find_all with 'a' tag and class 'job-title'
    urls = []
    for urls_elem in parser.find_all('h2', class_="h5 mb-0 mr-2 job-tile-title"):
        urls.append(urls_elem.a['href'])

    # Extract descriptions using a loop for better readability
    descriptions = []
    for desc_elem in parser.select('section article div div div div p'):
        descriptions.append(desc_elem.text)

    # print(titles)
    # print(urls)
    # print(descriptions)

    # Making a list of dicts
    for i in range(10):
        job = f"{{ 'title' : '{titles[i]}', 'url' : 'https://upwork.com{urls[i]}' , 'description' : '''{descriptions[i]}''' }}"
        jobs.append(eval(job))
    return jobs

print(scrape_data())
