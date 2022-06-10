
import requests, sys, re
from urllib.parse import urlparse

target_url = str(sys.argv[1])
target_links = []

def extract_links(url):
   response = requests.get(target_url)
   # regex: looks for href=" and then takes everything up until the next "
   return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))

# Recursive crawl
def crawl(url):
   href_links = extract_links(url)
   for link in href_links:
      # converts to proper url format
      link = urlparse.urljoin(url, link)

      if "#" in link:
         link = link.split("#")[0]

      if target_url in link and link not in target_links:
         target_links.append(link)
         print(link)
         crawl(link)

crawl(target_url)