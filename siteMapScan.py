from bs4 import BeautifulSoup
import requests

"""
Script scans the blog sitemap and returns each
[slug, last modified date, image url, image url, image url, ...]
The purpose is to get the slug and image urls for each blog,
then we can use the slug to scrape the blog page and get the title,
and then we can use the image urls to download the images
"""

#We are going to scrape zenpayments.com's pages
headers = {
    "User-Agent": "Blog Scraper https://github.com/juderhall/codespaces-get_blog_info)",
    "Email": "nick@zenpayments.com"
}

web_address = "https://zenpayments.com/post-sitemap.xml"
#scrape the address
response = requests.get(web_address, headers=headers)
if response.ok:
    soup = BeautifulSoup(response.text, features="xml").prettify()
    soup = soup.split('<url>')
    unLovedTags = ['</url>', '</urlset>', '</loc>', '</lastmod>', '</image:image>', '</image:loc>', '<!-- XML Sitemap generated by Yoast SEO -->']
    for blog in range(len(soup)):
        #Check for one of the unloved tags in plethora of text
        for tag in unLovedTags:
            if tag in soup[blog]:
                soup[blog] = soup[blog].replace(tag, '')
    soup = soup[1:]
    sauce = 0
    for souper in range(len(soup)):
        #Splitting on the loc tag
        soup[souper] = soup[souper].split('<loc>')
        #Getting rid of the white space, newlines, all the tagz
        soup[souper] = soup[souper][1:][0].replace('\n', '').replace('<image:loc>', '').replace('<image:image>', '').replace('<lastmod>', '').strip().split(' ')
        #Now we have a list of tags, remove the empty elements
        while('' in soup[souper]):
            soup[souper].remove('')
    #This is looking like a more delicious soup isnt it?
    for url in range(len(soup)): soup[url][0] = soup[url][0].replace('https://zenpayments.com/', '').replace('/', '')
    for x in soup: print(x[0])   