import requests
import re
from bs4 import BeautifulSoup,NavigableString

def getBlogLayout(slug: str) -> list:
    headers = { "User-Agent": "Blog Scraper https://github.com/juderhall/codespaces-get_blog_info)", "Email": "nick@zenpayments.com"}
    response = requests.get(f'https://zenpayments.com/{slug}/', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    #element 0 is the header, 1 is the body, 2 is the footer
    soup = soup.find_all('div', {'class': "elementor-container elementor-column-gap-default"})[1]
    unlovedElements = ['form', 'style', 'link', 'section']
    for unlovedElement in unlovedElements:
        for element in soup.find_all(unlovedElement):
            element.decompose()
    
    #Recursively unfolding all of the divs
    for tag in soup.find_all('div', class_=lambda x: x and 'elementor' in x):
        tag.unwrap()
    
    #Now that we unwrapped important elements, we can remove the rest of the divs
    for poopySoup in soup.find_all('div'):
        poopySoup.decompose()

    #Remove all the spans
    for span in soup.find_all('span'):
        span.unwrap()

    # Remove empty p tags
    for p in soup.find_all('p'):
        if not p.text.strip():  # if the p tag has no text
            p.decompose()
    
    # Remove <br> tags
    for br in soup.find_all('br'):
        br.unwrap()

   # Remove elements that are not wrapped in a heading, paragraph or image tag, or bolded
    for content in soup.contents:
        if isinstance(content, NavigableString):
            content.extract()
        elif content.name not in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'img', 'b', 'ol']:
            content.decompose()

    #Remove the navigation buttons at the bottom of the page
    for a in soup.find_all('a', rel='prev'):
        a.decompose()
    for a in soup.find_all('a', rel='next'):
        a.decompose()

    #Remove specific attributes from the tag
    for tag in soup.find_all(True):
        attrs_to_delete = ['class', 'height', 'width', 'loading', 'sizes', 'srcset', 'style', 'aria-level', 'decoding', 'rel']
        for attr in attrs_to_delete:
            del tag[attr]
    
    #Removing the parent div tag
    output = soup.prettify()

    #--Going to a string object below--
    body = re.split(r"<div class=\"elementor-container elementor-column-gap-default\">|</div>", output)
    
    #Filtering newlines, spaces, and empty strings
    body = [part for part in body if part not in ['\n', ' ', '']]
    body = body[0].replace('\n', '')
    #Normalizing all of the spaces between the tags to 1 space ' '
    body = re.sub(r"\s+", ' ', body)
    #Removing the leading and trailing spaces
    body = body.strip()
    #Eliminating spaces between open and close tags
    body = body.replace('> ', '>').replace(' <', '<')

    #Back to a soup object to parse the HTML, 1 level deep
    body = BeautifulSoup(body, 'html.parser')
    level_one_tags = [child for child in body.children if child.name]
    body = [str(tag) for tag in level_one_tags]
    return body


    
