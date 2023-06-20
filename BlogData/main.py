#main program
import siteMapScan
import scaper
import json

def main():
    #Pull the images and alt text
    allBlogInfo = []
    blogSlugsAndDates = siteMapScan.scrapeBasicBlogInfo()
    print(blogSlugsAndDates)
    for blogInfo in blogSlugsAndDates: 
        slug = blogInfo[0]
        date = blogInfo[1].split('+')[0]
        print(f"Scraping {slug}")
        #scrape the blog
        try:
            blogData = scaper.getBlogLayout(slug)
            for x in blogData: print(x, '\n')
            allBlogInfo.append(
                {
                    'slug': slug, 
                    'date': date,
                    'blogData': blogData,
                    'succes': True
                }
            )
            print(f"Scraped {slug}")
        except:
            allBlogInfo.append(
                {
                    'slug': slug,
                    'date': date,
                    'blogData': None,
                    'succes': False
                }
            )
            print(f"Failed to scrape {slug}")
    #Dump the data to a json file
    with open('./blogInfo.json', 'w') as f:
        json.dump(allBlogInfo, f, indent=4)



if __name__ == "__main__":
    main()
