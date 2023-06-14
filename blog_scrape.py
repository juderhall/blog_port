from urllib.parse import urlparse

# create a function to extract the slug from the web address
def extract_slug(web_address):
    parsed_url = urlparse(web_address)
    slug = parsed_url.path
    print(slug)

# scrapes content off blog page and prints to console 
def extract_specific_text(soup):
    tags = ['a','h1', 'h2', 'h3', 'li', 'p',]
    
    exclude_header = soup.find('div', {'data-elementor-type': 'header'})
    exclude_footer = soup.find('div', {'data-elementor-type': 'footer'})

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