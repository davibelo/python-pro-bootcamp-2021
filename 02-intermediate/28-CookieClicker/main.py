from selenium import webdriver
from time import time

chrome_driver_path = "/home/davibelo/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

#Get cookie to click on.
cookie = driver.find_element_by_id("cookie")

game_timeout = time() + 60 * 5
buy_item_timeout = time() + 5

# --- Getting Upgrades --- #

item_tags = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in item_tags]

item_price_tags = driver.find_elements_by_css_selector("#store b")
item_price_texts = [item.text for item in item_price_tags]

item_prices = []
for item in item_price_texts:
    if item != "":
        item_prices.append(int(item.split("-")[1].strip().replace(",", "")))

upgrades = {}
for i in range(0, len(item_prices)):
    upgrades[item_ids[i]] = item_prices[i]


driver.quit()