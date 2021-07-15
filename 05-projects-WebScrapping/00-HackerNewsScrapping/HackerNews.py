from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tags = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in article_tags:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))

article_upvotes = [
    int(score.getText().split(" ")[0])
    for score in soup.find_all(name="span", class_="score")
]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

largest_upvotes_index = article_upvotes.index(max(article_upvotes))

largest_upvotes_text = article_texts[largest_upvotes_index]
largest_upvotes_link = article_links[largest_upvotes_index]
print(largest_upvotes_text)
print(largest_upvotes_link)