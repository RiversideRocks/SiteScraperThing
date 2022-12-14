import requests
from bs4 import BeautifulSoup
import time
import os

print("Clearing old files out from directory")
f = os.listdir('lists')
for stuff in f:
    if ".txt" in stuff:
        os.remove('lists/' + stuff)
        print("Destroyed " + str(stuff))

print("Downloading from the archive.org via the Wayback Machine...")
print("This may take a long time!")
time.sleep(5)

url = "https://web.archive.org/web/20220328132419/https://dataset.domainsproject.org/generic_com/"
html = requests.get(url, headers={"User-agent": "RiversideRocks (+https://riverside.rocks)"})
soup = BeautifulSoup(html.text, "html.parser")
links = soup.find_all('a')
file = 0
for link in links:
    if ".txt" in link['href']:
        href = requests.get("https://web.archive.org/web/20220328142042if_/https://dataset.domainsproject.org/generic_com/" + link['href'], headers={"User-agent": "RiversideRocks (+https://riverside.rocks)"})
        print("GET /" + link['href'] + " - " + str(href.status_code))
        write_to = open('lists/dataset_' + str(file) + '.txt', 'a')
        write_to.write(href.text)
        write_to.close()
        file = file + 1