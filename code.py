import requests
from pyquery import PyQuery as pq
response = requests.get('https://www.macrotrends.net/1369/crude-oil-price-history-chart')

infoset = []
doc = pq(response.text)
doc.make_links_absolute(base_url=response.url)

for data in doc("#style-1 > table > tbody tr:nth-child(n)").items():
    infoDict = {}
    infoDict["Year"] = data("td:nth-child(1)").text()
    infoDict["Price"] = data("td:nth-child(2)").text()
    infoset.append(infoDict)

a = int(input())
b = int(input())
result = []
for i in range (2020-a,2020-b+1):
    result += [infoset[i]]
    
result.sort(key=lambda k: (k.get('Price', 0), k.get('Year', 0)), reverse=False)

for i in result:
    print('year:{}, price:{}'.format(i["Year"],i["Price"]))
