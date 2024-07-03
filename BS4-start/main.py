from bs4 import BeautifulSoup
import requests


response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article_tag in articles:
    text= article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


print(article_texts)
print(article_links)
print(article_upvotes)

largest_upvote = max(article_upvotes)
print(largest_upvote)
largest_upvote_index = article_upvotes.index(largest_upvote)
print(f"The most upvote article is: ", article_texts[largest_upvote_index])
print(f"Check out the most upvote recent article: ", article_links[largest_upvote_index])