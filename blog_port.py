from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

# create a function to extract specific tags from a blog, and store them in a dictionary in the order they appear
def extract_specific_text(soup):
    tags = ['a','h1', 'h2', 'h3', 'li', 'p',]
    
    exclude_header = soup.find('div', {'data-elementor-type': 'header'})
    exclude_footer = soup.find('div', {'data-elementor-type': 'footer'})
    exclude_widget = soup.find('section', {'class': 'elementor-section elementor-inner-section elementor-element elementor-element-11e3c129 elementor-hidden-mobile elementor-section-boxed elementor-section-height-default elementor-section-height-default elementor-sticky elementor-sticky--active elementor-section--handles-inside elementor-sticky--effects'})
    
    dict = {}
    x = 0

    for element in soup.find_all(tags):
        if element in exclude_header.descendants:
            continue
        if element in exclude_footer.descendants:
            continue
    
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
