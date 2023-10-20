from bs4 import BeautifulSoup as bs
import requests

def getUrls():
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=ampharos+prime&_sacat=0&_sop=15'

    # Get the page
    page = requests.get(url)

    # Parses the html as text
    soup = bs(page.text,'html5lib')
    urlList = []
    #Find the div where the URL is stored
    divs = soup.find_all("div", {"class": "s-item__info clearfix"})
    #Find the a tag
    for link in divs:
        links = link.find("a")
        #If a href is found, then append to list
        if links:
            href = links.get('href')
            urlList.append(href)
    #Remove the top element as it is not part of the search
    urlList.pop(0)
    return urlList

#Get the string of the price, and return only the number
def getNumber(string):
    temp = string.partition(" ")[2]
    if '$' in temp:
        temp = temp.partition('$')[2]
    return(temp)

#Add together the two strings of price and shipping
def addTogether(str1, str2):
    if str2 == '':
        return round(float(str1), 2)
    final = (float(str1) + float(str2))
    return round(final, 2)

#Get price for each URL in list
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
        #Add the price and shipping together
        fullPrice = addTogether(price, shipping)
        #Append price to list
        priceList.append(fullPrice)
    print(priceList)

url = getUrls()
getPrice(url)
