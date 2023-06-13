from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

# create a function to extract the visible text from the web page
def extract_visible_text(soup):
    text = [element.text.replace('\n', ' ') for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'li'])]
    text_string = ' '.join(text)
    print(text_string)
    # count the words in the text_string
    word_count = len(text_string.split())
    print(word_count)

# create a function to extract specific text from the web page with tags 
def extract_specific_text(soup):
    tags = ['h1', 'h2',]
    dict = {}
    x = 0

    for element in soup.find_all(tags):
        dict [x] = [element.name, element.text]
        x += 1
    print(dict)

# create a function to extract the image urls from the web page
def extract_image_urls(soup):
    images = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs]
    for image in images:
        print(image)

# create a function to extract the slug from the web address
def extract_slug(web_address):
    parsed_url = urlparse(web_address)
    slug = parsed_url.path
    print(slug)

# create varible to hold the url
web_address = "https://zenpayments.com/virtual-merchant/"

# create a variable to hold the headers
headers = {
    'User-Agent' : 'Blog Scraper (https://github.com/juderhall/codespaces-get_blog_info)',
    'Email' : 'jude@zenpayments.com'
}

# create a variable to hold the response
response = requests.get(web_address, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    extract_specific_text(soup)
else:
    print("Failed to fetch the web page. Status code:", response.status_code)

"""
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    extract_slug(web_address)
    extract_visible_text(soup)
    extract_image_urls(soup)
else:
    print("Failed to fetch the web page. Status code:", response.status_code)
"""