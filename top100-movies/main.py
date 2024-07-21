import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
print(response)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup)

all_movies = soup.find_all(name="h3", class_="title")
# print(all_movies)

# extract all the movies from the website and list them
movie_title = [movie.getText() for movie in all_movies]
print(movie_title[95:5:-5])
movies = movie_title[::-1]

# for n in range(len(movie_title) -1, -1, -1):
#     print(movie_title[n])

# write the movies into a file
with open("movies.txt", mode="w", encoding='utf-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")
