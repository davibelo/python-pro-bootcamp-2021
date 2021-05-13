from bs4 import BeautifulSoup

WEB_PAGE = "https://www.empireonline.com/movies/features/best-movies-2/"
WEB_FILE = "02-intermediate/25-WebScraping/100_best_movies.html"

# because this web page uses javascript to render the page dinamically
# and the html is not in the source code, it is
# necessary to download the page and make the scrapping after
# use javascript on webpage console to copy html generated to clipboard: 
# copy(document.querySelector('html').outerHTML)


def read_web_file():
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        print(f"You need to save the rendered HTML to {WEB_FILE}")
        exit()
    finally:
        # Read the web page from file
        with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
            content = fp.read()
        return BeautifulSoup(content, "html.parser")


# Read web file if it exists, load from internet if it doesn't exist
soup = read_web_file()

movie_tags = soup.find_all(name="h3")
print(movie_tags)