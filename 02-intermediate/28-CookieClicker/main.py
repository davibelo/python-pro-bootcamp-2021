from selenium import webdriver
from time import time

chrome_driver_path = "/home/davibelo/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

TOTAL_GAME_TIME = 60
BUY_TIME = 5

# get cookie to click on.
cookie = driver.find_element_by_id("cookie")

# setting times
start_time = time()
game_end_time = start_time + TOTAL_GAME_TIME
buy_item_timeout = start_time + BUY_TIME


def get_upgrades():
    """returns a dict with upgrades ids and prices"""
    # getting ids
    item_tags = driver.find_elements_by_css_selector("#store div")
    item_ids = []
    for item in item_tags:
        item_id = item.get_attribute("id")
        if item_id != "":
            item_ids.append(item_id)
    # getting prices
    item_price_tags = driver.find_elements_by_css_selector("#store b")
    item_prices = []
    for item in item_price_tags:
        price = item.text
        if price != "":
            cost = int(price.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)
    # making upgrade dict
    upgrades = {}
    for i in range(len(item_prices)):
        upgrades[item_ids[i]] = item_prices[i]
    return upgrades


def get_money():
    """returns actual money"""
    money_tag = driver.find_element_by_id("money")
    return int(money_tag.text.split()[0].replace(",", ""))


continue_game = True

while continue_game == True:
    cookie.click()

    if time() > buy_item_timeout:
        upgrades = get_upgrades()
        money = get_money()
        
        affordable_upgrades = {}
        affordable_upgrades = {
            key: value
            for (key, value) in upgrades.items() if value < money
        }
        print(affordable_upgrades)

        #FIXME: not getting most expensive upgrade
        most_expensive_upgrade_id = max(affordable_upgrades)
        print(most_expensive_upgrade_id)

        # upgrade_to_buy_tag = driver.find_element_by_id(
        #     most_expensive_upgrade_id)
        # upgrade_to_buy_tag.click()

        buy_item_timeout = time() + BUY_TIME

    if time() > game_end_time:
        continue_game = False

driver.quit()