from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

sidoDic = {1: 25, 2: 16, 3: 8, 4: 10, 5 : 5, 6: 5, 7: 5, 8: 16, 9: 44, 10: 18, 11: 15, 12: 17, 13: 15, 14: 22, 15: 24, 16: 22, 17: 2}
result = []

for sido1, sido2 in sidoDic.items():
    kyochonURL = "https://www.kyochon.com/shop/domestic.asp?sido1=" + str(sido1)

    for sido2Idx in range(1, sido2 + 1):
        kyochonURL += "&sido2="+ str(sido2Idx) +"&txtsearch="

        html = urllib.request.urlopen(kyochonURL)
        soup = BeautifulSoup(html, "html.parser")

        for store in soup.find_all('span', 'store_item'):
            storeName = store.find('strong').string
            storeInfo = store.find('em').text.strip().split("\n")
            storeAddress = storeInfo[1].strip()[1 : -1]

            if storeAddress == "":
                storeAddress = storeInfo[0].strip()[1 : -1]

            storeSido = storeAddress.split()[0]
            storeGungu = storeAddress.split()[1]

            print(storeName + " : " + storeSido + " " + storeGungu + " " + storeAddress)
            result.append([storeName] + [storeSido] + [storeGungu] + [storeAddress])

        kyochonURL = "https://www.kyochon.com/shop/domestic.asp?sido1=" + str(sido1)

kyochonTable = pd.DataFrame(result, columns=['store', 'sido', 'gungu', 'address'])
kyochonTable.to_csv('C:\\Users\joung\Downloads\kyochon.csv', encoding = 'utf-8-sig', mode = 'w', index = True)