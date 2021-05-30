from selenium import webdriver
chrome_driver_path = "/home/davibelo/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# click example 1
article_count = driver.find_element_by_css_selector("#articlecount a")
# article_count.click()

# click example 2
all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()





# driver.quit()

