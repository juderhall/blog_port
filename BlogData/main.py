#main program
import siteMapScan
import scaper
import json

def main():
    #Pull the images and alt text
    allBlogInfo = []
    blogSlugsAndDates = siteMapScan.scrapeBasicBlogInfo()
    for blogInfo in blogSlugsAndDates: 
        slug = blogInfo[0]
        date = blogInfo[1].split('+')[0]
        #scrape the blog
        try:
            blogData = scaper.getBlogLayout(slug)
            blogBody = blogData['body']
            title = blogData['title'].decode_contents()
            blogDescription = blogData['meta'].get('content')
            allBlogInfo.append(
                {
                    'slug': slug,
                    'title': title,
                    'metaDescription': blogDescription, 
                    'date': date,
                    'blogBody': blogBody,
                    'succes': True
                }
            )
            print(f"Scraped {slug}")
        except:
            allBlogInfo.append(
                {
                    'slug': slug,
                    'date': date,
                    'blogBody': None,
                    'succes': False
                }
            )
            print(f"Failed to scrape {slug}")
    #Dump the data to a json file
    with open('./blogInfo.json', 'w') as f:
        json.dump(allBlogInfo, f, indent=4)



if __name__ == "__main__":
    main()
