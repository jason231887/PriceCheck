from bs4 import BeautifulSoup as bs
import requests

fullList = []
urlList = []
maxList = []
length = 0

def getLinks():
    global length
    input = open('input.txt', 'r')
    for each in input:
        url = each.partition(',')[0]
        max = each.partition(',')[2]
        urlList.append(url)
        maxList.append(max)
        length = length + 1
    input.close()

def getListings(url):
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
def getPrice(urls, max):
    max = float(max)
    global fullList
    page = requests.get(urls)
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
    if type(shipping) != 'float':
        fullPrice = price
    else:
        fullPrice = addTogether(price, shipping)
    fullPrice = float(fullPrice)
    if fullPrice > max:
        return False
    #Append price to list
    fullList.append([urls, fullPrice])
    return True
#Main
getLinks()
for each in range(length):
    url = getListings(urlList[each])
    for link in url:
        if (getPrice(link, maxList[each])):
            continue
        else: 
            break

output = open("output.txt",'w')
for each in fullList:
    output.write(str(each))
output.close()
print(fullList)
