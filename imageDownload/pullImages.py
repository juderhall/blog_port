#The purpose of this file is to download the images from the blog posts
#We are going to multithread this process because it is extremely slow
import requests
import os
import threading
import json

with open('../siteMapScan/siteInfo.json', 'r') as file:
    file = json.parse(file.read())
    print(file)