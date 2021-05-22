import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import smtplib

PRICE_ALERT = 300
AMAZON_URL = "https://www.amazon.com.br/NieR-Replicant-ver-1-22474487139-PlayStation/dp/B08XXJ4ZGP/ref=pd_rhf_gw_s_pd_crcd_28/143-3317859-4399827?pd_rd_w=Vw1jM&pf_rd_p=49e26231-6534-4f40-8a6b-8528d27191f2&pf_rd_r=EBMRF9Q22KQ0EB2J87B8&pd_rd_r=2a285224-1df7-4c9f-83a5-40c4ce41ba51&pd_rd_wg=ESx6v&pd_rd_i=B08XXJ4ZGP&psc=1"
DEST_EMAIL = "davibelo@gmail.com"

# --- Scraping Amazon Price --- #

headers = {
    "Accept-Language":
    "en-US,en;q=0.5",
    "User-Agent":
    "Mozilla/5.0 (X11; Linux aarch64; rv:78.0) Gecko/20100101 Firefox/78.0"
}

print("checking product price...")
response = requests.get(url=AMAZON_URL, headers=headers)
amazon_website = response.text
soup = BeautifulSoup(amazon_website, "html.parser")

product_tag = soup.find_all(name="span", id="productTitle")
product = product_tag[0].getText().replace("\n", "")
print(product)

price_tag = soup.find_all(name="span", id="priceblock_ourprice")
price = float(price_tag[0].getText()[2:-3])

# --- Checking price and sending email --- #

# loading constants
REL_PATH = os.path.dirname(__file__)
load_dotenv(dotenv_path=f"{REL_PATH}/.env")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_EMAIL_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")

if price < PRICE_ALERT:
    print("sending email...")
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=DEST_EMAIL,
            msg=
            f"Subject:Deal on {product}!\n\nYour product have a good price!\nlink: {AMAZON_URL}\n\nDaviBot"
        )
    print(f"email sent to {DEST_EMAIL}!")
else:
    print("product price > alert price! No email sent")
