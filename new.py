from bs4 import BeautifulSoup as bs
import requests
import decimal

maxPrice = 10
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

def getNumber(string):
    temp = string.partition(" ")[2]
    if '$' in temp:
        temp = temp.partition('$')[2]
    return(temp)

def addTogether(str1, str2):
    if str2 == '':
        return round(float(str1), 2)
    final = (float(str1) + float(str2))
    return round(final, 2)

def getPrice(urls):
    priceList = []
    for url in urls:
        page = requests.get(url)
        soup = bs(page.text,'html5lib')
        #Get the price of the item
        priceDiv = soup.find("div", {"class": "x-price-primary"})
        price = priceDiv.find("span", {'class' : 'ux-textspans'}).text
        price = getNumber(price)
        #Get the price of shipping
        shippingDiv = soup.find("div", {"class": "ux-labels-values__values-content"})
        shipping = shippingDiv.find("span", {'class' : 'ux-textspans ux-textspans--BOLD'}).text
        shipping = getNumber(shipping)

        fullPrice = addTogether(price, shipping)
        priceList.append(fullPrice)
    print(priceList)

url = getUrls()
getPrice(url)