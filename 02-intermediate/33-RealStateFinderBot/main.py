import os
from selenium import webdriver
import pandas as pd

REL_PATH = os.path.dirname(__file__)
CHROME_DRIVER_PATH = "/home/davibelo/chromedriver"
URL = "https://rj.olx.com.br/rio-de-janeiro-e-regiao/zona-oeste/jacarepagua/imoveis/aluguel/apartamentos?pe=5000&ps=2000&ros=3&sp=2&ss=3"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(URL)

titles_raw = []
links_raw = []
neighborhoods_raw = []

titles = []
links = []
neighborhoods = []


def get_info():
    """
    get information on loaded page
    """
    anchor_tags = driver.find_elements_by_css_selector("ul#ad-list li a")
    for anchor_tag in anchor_tags:
        title = anchor_tag.get_attribute("title")
        if title == "":
            pass
        else:
            titles_raw.append(title)
    for anchor_tag in anchor_tags:
        link = anchor_tag.get_attribute("href")
        if not "olx.com.br" in link:
            pass
        else:
            links_raw.append(link)

    span_tags = driver.find_elements_by_css_selector("ul#ad-list li a span")

    for span_tag in span_tags:
        if not "Rio de Janeiro, " in span_tag.text:
            pass
        else:
            neighborhoods_raw.append(span_tag.text)


def print_lengths():
    print(len(titles_raw), len(links_raw), len(neighborhoods_raw))


# --- scrapping --- #

get_info()
print_lengths()
next_page_button = driver.find_element_by_link_text("Próxima pagina")
next_page_button.click()
get_info()
print_lengths()

driver.close()

for i in range(len(titles_raw)):    
    if "Jacare" in neighborhoods_raw[i]:
        titles.append(titles_raw[i])
        links.append(links_raw[i])
        neighborhoods.append(neighborhoods_raw[i])

print(titles)
print(links)
print(neighborhoods)
