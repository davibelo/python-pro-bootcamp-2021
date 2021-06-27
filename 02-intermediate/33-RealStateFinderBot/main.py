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
    print("getting titles...")
    for anchor_tag in anchor_tags:
        title = anchor_tag.get_attribute("title")
        if title == "":
            pass
        else:
            titles_raw.append(title)
    print("getting links...")
    for anchor_tag in anchor_tags:
        link = anchor_tag.get_attribute("href")
        if not "olx.com.br" in link:
            pass
        else:
            links_raw.append(link)
    span_tags = driver.find_elements_by_css_selector("ul#ad-list li a span")
    print("getting neighborhoods...")
    for span_tag in span_tags:
        if not "Rio de Janeiro, " in span_tag.text:
            pass
        else:
            neighborhoods_raw.append(span_tag.text)


def print_lengths():
    print("raw ads: ", len(titles_raw), len(links_raw), len(neighborhoods_raw))
    print("filtered_ads: ",len(titles), len(links), len(neighborhoods))


# --- START --- #

get_info()
print_lengths()
next_page_button = driver.find_element_by_link_text("Próxima pagina")
next_page_button.click()
get_info()
print_lengths()

driver.close()

print("filtering information...")
for i in range(len(titles_raw)):
    if "Jacarepaguá" in neighborhoods_raw[i]:
        titles.append(titles_raw[i])
        links.append(links_raw[i])
        neighborhoods.append(neighborhoods_raw[i])

print_lengths()
# print(titles)
# print(links)
# print(neighborhoods)

ads_dict = {
    "titles": titles,
    "neighborhood": neighborhoods,
    "links": links
}

ads_df = pd.DataFrame.from_dict(ads_dict)
print(ads_df.head())

print("saving files...")
writer = pd.ExcelWriter(f"{REL_PATH}/aptos.xlsx", engine="xlsxwriter")
ads_df.to_excel(writer, sheet_name="Sheet1")
writer.save()
ads_df.to_csv(f"{REL_PATH}/aptos.csv")