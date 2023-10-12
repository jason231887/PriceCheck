from bs4 import BeautifulSoup as bs
import requests
from time import gmtime, strftime
import shutil
import re

def getUrls():
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2332490.m570.l1313&_nkw=absol&_sacat=0'

    # Get the page
    page = requests.get(url)

    # Parses the html as text
    soup=bs(page.text,'html5lib')
    #Create list for all the urls
    list = []

    for link in soup.find_all('a', attrs={'href': re.compile("^https://www.ebay.com/itm/")}):
        list.append(link.get('href'))   
    print(list)
    print(len(list))

def getImage():

    #Link of the store page
    url = 'https://www.ebay.com/itm/404433261695?hash=item5e2a19d47f:g:3HUAAOSwH5tk1Y8z&amdata=enc%3AAQAIAAAAwLMLX4qoxVFMtyllNGzWIwFcC8tHTM7C7VbUMMZgyBkWeecEy%2BjQB8XD1NE%2FSa5%2BU3JQ1x0jc3fCh8eqH5CsiCLQ03Ij4ij19VCbEft2tU%2B2y1seTJmkEGoQZBvSrBmoWCe97Ued%2BCIeE4VnS5%2B00Neg135qzdmE5xq3lq5i86edVlpXUU%2FiUUKh0hul8WowiOfnnv%2BJA8Q5pUnWLswQfNG%2FYv8SyH%2FQPqNOaWRVxVGEjOlzJJQnJ9ZSyBsNnoovhA%3D%3D%7Ctkp%3ABk9SR67ljILkYg'

    # Get the page
    page = requests.get(url)

    # Parses the html
    soup = bs(page.text, 'html5lib')

    #Get the image
    link = soup.find_all('div', {'class': 'image'})
    
    #Get the url for the image
    if link:
        link = (link[0].find('img')['src'])
    
    #Get the request for the image
    r = requests.get(link, stream=True)
    #If image is OK, then decode, then save to local
    if r.status_code == 200:
        with open("file.png", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
getImage()