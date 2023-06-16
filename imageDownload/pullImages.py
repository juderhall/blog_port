import requests
import os
import threading
import json
import pullAltText
import siteMapScan
siteInfo = siteMapScan.scrapeBasicBlogInfo()
#Collect the slug, date published, and image url
#We are also going to need to scrape the image alt tags in another program...
booboo = 0
for x in siteInfo:
    curIdx = siteInfo.index(x)
    newImages = pullAltText.getAltTags(x[0], x[2:])
    x = x[:2] ; x.append(newImages)
    siteInfo[curIdx] = x
    booboo += 1
    if (booboo > 10): break

#Testing please delete later
siteInfo = siteInfo[0:11]
#Download the images (O^3 complexity lol)
for info in siteInfo:
    for image in info[2]:
        for url in image:
            try:
                r = requests.get(url, allow_redirects=False, headers={'user-agent': 'Mozilla/5.0'})
                if r.status_code == 200:
                    with open(f"./images/{url.split('/')[-1]}", 'wb') as f:
                        f.write(r.content)
            except:
                #PICK UP HERE
                print(f"Failed to download {url}")
#TODO Replace the links in the siteInfo with the local links

