from bs4 import BeautifulSoup as bs
import requests

def getPrices():
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=ampharos+prime&_sacat=0&_sop=15'

    # Get the page
    page = requests.get(url)

    # Parses the html as text
    soup = bs(page.text,'html5lib')
    
    priceList = []
    prices = soup.find_all("span", {'class' : 's-item__price'})
    for price in prices:
        temp = str(price)
        dollar = temp.partition("$")[2]
        final = dollar.partition("<")
        priceList.append(final[0])
    priceList.pop(0)
    print(priceList)

def getUrls():
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=ampharos+prime&_sacat=0&_sop=15'

    # Get the page
    page = requests.get(url)

    # Parses the html as text
    soup = bs(page.text,'html5lib')
    urlList = []
    divs = soup.find_all("div", {"class": "s-item__info clearfix"})
    for link in divs:
        links = link.find("a")
        if links:
            href = links.get('href')
            urlList.append(href)
    urlList.pop(0)
    #print(urlList)
    return urlList

def getPrice(urls):
    priceList = []
    for url in urls:
        page = requests.get(url)
        soup = bs(page.text,'html5lib')
        priceDiv = soup.find("div", {"class": "x-price-primary"})
        price = priceDiv.find("span", {'class' : 'ux-textspans'}).text
        shippingDiv = soup.find("div", {"class": "ux-labels-values__values-content"})
        shipping = shippingDiv.find("span", {'class' : 'ux-textspans ux-textspans--BOLD'}).text
        fullPrice = price + " + " + shipping
        priceList.append(fullPrice)
    print(priceList)

url = getUrls()
getPrice(url)