import requests
import pullAltText
import siteMapScan

def getTotalImageInfo(test: bool) -> dict:
    headers = { "User-Agent": "Blog Scraper https://github.com/juderhall/codespaces-get_blog_info)", "Email": "nick@zenpayments.com"}
    siteInfo = siteMapScan.scrapeBasicBlogInfo()
    #Collect the slug, date published, and image url
    #We are also going to need to scrape the image alt tags in another program...
    testMax = 0
    for x in siteInfo:
        curIdx = siteInfo.index(x)
        newImages = pullAltText.getAltTags(x[0], x[2:])
        x = x[:2]
        x.append(newImages)
        siteInfo[curIdx] = x
        testMax += 1
        if (testMax > 10 and test): break

    #Testing please delete later
    siteInfo = siteInfo[0:11]
    newSiteInfo = {}
    #Download the images (O^3 complexity lol)
    localFileName = ''
    for info in siteInfo:
        newSiteInfo[info[0]] = {'date': info[1], 'images': []}
        for image in info[2]:
            for url in image:
                r = requests.get(url, allow_redirects=False, headers=headers)
                if r.ok:
                    #Download the images
                    localFileName = url.split('/')[-1]
                    with open(f"imageDownload/images/{localFileName}", 'wb') as file:
                        file.write(r.content) 
                    newSiteInfo[info[0]]['images'].append({'url': url, 'localName': localFileName, 'altText': image[url]})
    #OK now we have all of our images containerized, time to scrape the blogs
    return newSiteInfo    
newSiteInfo = getTotalImageInfo(True)

for x in newSiteInfo:
    print(x, newSiteInfo[x])
