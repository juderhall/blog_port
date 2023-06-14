from blog_scrape import extract_specific_text, extract_slug
from bs4 import BeautifulSoup
import requests

# create a variable to hold the headers
headers = {
    'User-Agent' : 'Blog Scraper (https://github.com/juderhall/codespaces-get_blog_info)',
    'Email' : 'jude@zenpayments.com'
}   

# create varible to hold the url
web_address = "https://zenpayments.com/virtual-merchant/"

# create a variable to hold the response
response = requests.get(web_address, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print(extract_slug(web_address), extract_specific_text(soup))
else:
    print("Failed to fetch the web page. Status code:", response.status_code)
