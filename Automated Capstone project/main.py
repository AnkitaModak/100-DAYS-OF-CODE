import time
import lxml
from bs4 import BeautifulSoup
import requests
from google_form import fill_form
url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url)
zillow_page = response.text
soup= BeautifulSoup(markup=zillow_page, parser="html.parser" , features="lxml")
get_prices = soup.find_all("span",class_="PropertyCardWrapper__StyledPriceLine")
get_links =soup.find_all(name="a" , class_="StyledPropertyCardDataArea-anchor")
get_addresses = soup.find_all(name="address")
prices = [price.getText().split("+")[0].strip() for price in get_prices]
links = [link.get("href") for link in get_links]
addresses = [address.getText().strip() for address in get_addresses]
print(addresses)
for n in range(len(prices)):
    fill_form(address=addresses[n] , price=prices[n] ,link = links[n])

