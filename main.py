from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from scraping_listings import ListingsScraper

CHROME_DRIVER_PATH = "/Development/chromedriver"
GOOGLE_FORM_URL = "https://docs.google.com/forms/" \
            "d/e/1FAIpQLSfm0zbEiuyXX7umwD3h15jlRr_RcheGqvl-XkU904ffsQs3vw/viewform?usp=sf_link"


scraper = ListingsScraper()
links = scraper.get_links()
prices = scraper.get_prices()
addresses = scraper.get_addresses()

print(links)
print(prices)
sleep(2)

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get(GOOGLE_FORM_URL)
driver.maximize_window()
sleep(4)

address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]'
                                              '/div/div/div[2]/div/div[1]/div/div[1]/input')
price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]'
                                            '/div/div/div[2]/div/div[1]/div/div[1]/input')
link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]'
                                           '/div/div/div[2]/div/div[1]/div/div[1]/input')
submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

for i in range(len(addresses)):
    address_input.send_keys(addresses[i])
    price_input.send_keys(prices[i])
    link_input.send_keys(links[i])
    submit_btn.click()
    sleep(1)
