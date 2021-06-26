import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import ElementClickInterceptedException

REL_PATH = os.path.dirname(__file__)
CHROME_DRIVER_PATH = "/home/davibelo/chromedriver"
URL = "https://rj.olx.com.br/rio-de-janeiro-e-regiao/zona-oeste/jacarepagua/imoveis/aluguel/apartamentos?gsp=1&pe=6000&ros=3&sp=2"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(URL)

# # saving page source to use it with beautiful soup
# webpage = driver.page_source
# soup = BeautifulSoup(webpage, "html.parser")

# # saving source HTML to check if selenium got page source correctly
# prettyHTML = soup.prettify()
# with open(f"{REL_PATH}/website.html", mode="w") as file:
#     file.write(prettyHTML)


link_tags = driver.find_elements_by_css_selector("ul#ad-list li a")

titles = [tag.get_attribute("title") for tag in link_tags]
links = [tag.get_attribute("href") for tag in link_tags]
# title = link_tags[0].get_attribute("title")
# link = link_tags[0].get_attribute("href")

print(titles)
print(links)

driver.close()