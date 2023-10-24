from bs4 import BeautifulSoup as bs
import requests

#Final list to be output
fullList = []
#List of searches to be parsed
searchList = []
#List of max prices for each item
maxList = []
#The amount of searches in input.txt to be searched
length = 0

def getLinks():
    global length
    #Open input file of search urls
    input = open('input.txt', 'r')

    #Go through each line and grab the search link and max price
    for each in input:
        url = each.partition(',')[0]
        max = each.partition(',')[2]
        searchList.append(url)
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
    try:
        shipping = shippingDiv.find("span", {'class' : 'ux-textspans ux-textspans--BOLD'}).text
        shipping = getNumber(shipping)

    except Exception:
        shipping = None

    #If shipping isn't a float, then only take price into account
    if type(shipping) == float:
        fullPrice = addTogether(price, shipping)
    else:
        fullPrice = price

    #If price isnt a float, then skip the listing    
    try:
        fullPrice = float(fullPrice)
    except Exception:
        return False

    #If price is more than the max, then move onto next item
    if fullPrice > max:
        return False
    
    #Append price to list
    fullList.append(urls)
    return True

#Main

#Get search links from input.txt
getLinks()

#For each search URL, go through each item until max price is hit
for each in range(length):
    url = getListings(searchList[each])
    for link in url:
        if (getPrice(link, maxList[each])):
            continue
        #Max price has been hit, and move onto next item
        else: 
            break

#Open output file and write the list of URL's to it
output = open("output.txt",'w')
for each in fullList:
    output.write('%s\n' %each)
output.close()
print("DONE!")
