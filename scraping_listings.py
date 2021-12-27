import requests
from bs4 import BeautifulSoup

RENTAL_LISTINGS_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D" \
                      "%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22" \
                      "east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.8578770983" \
                      "16834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atru" \
                      "e%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22n" \
                      "c%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%" \
                      "22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3A" \
                      "false%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22" \
                      "price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible" \
                      "%22%3Atrue%2C%22mapZoom%22%3A12%7D"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": 'en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7'
}


class ListingsScraper:
    def __init__(self):
        self.response = requests.get(RENTAL_LISTINGS_URL, HEADERS)
        self.listings_webpage = self.response.text
        self.soup = BeautifulSoup(self.listings_webpage, "html.parser")

    def get_links(self):
        links_elements = self.soup.find_all(name="a", class_="list-card-link")
        links = []
        for i in range(len(links_elements)):
            links.append(links_elements[i]["href"].replace("/b/", "https://www.zillow.com/b/"))
        return links

    def get_prices(self):
        prices_elements = self.soup.find_all(class_="list-card-price")
        prices = [int(element.text.split()[0].replace("$", "").replace(",", "").replace("+", "").replace("/mo", ""))
                  for element in prices_elements]
        return prices

    def get_addresses(self):
        address_elements = self.soup.find_all(class_="list-card-addr")
        addresses = [element.text for element in address_elements]
        return addresses

