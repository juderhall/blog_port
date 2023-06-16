#This script will pull the alt text from the images and save it to a json file
#[{imgUrl: altText}, {imgUrl: altText}, {imgUrl: altText}...]

import requests
from bs4 import BeautifulSoup

def getAltTags(slug: str, image_urls: list) -> list:
    website_url = f'https://www.zenpayments.com/{slug}'
    headers = {
        'User-Agent' : 'Blog Scraper (https://github.com/juderhall/codespaces-get_blog_info)',
        'Email' : 'Nicolas Child'
    }   
    response = requests.get(website_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    alt_tags = []
    for img in soup.find_all('img'):
        if img['src'] in image_urls:
            if img['alt'] == '':
                alt_tags.append({img['src']: 'NO ALT TEXT!!'})
            else:
                alt_tags.append({img['src']: img['alt']})

    return alt_tags
